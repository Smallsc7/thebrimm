#!/usr/bin/env python3
"""Install or verify the complete package in one buyer-owned project. No network calls."""
import argparse, hashlib, json, os, re, shutil, sys, tempfile, uuid
from pathlib import Path

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def safe(root, relative):
    rel = Path(relative)
    if rel.is_absolute() or '..' in rel.parts:
        raise ValueError('Unsafe path in package: ' + relative)
    target = root / rel
    if target.is_symlink() or any(p.is_symlink() for p in target.parents if p != root.parent):
        raise ValueError('A symbolic link is in the installation path: ' + relative)
    if not target.resolve().is_relative_to(root.resolve()):
        raise ValueError('Path leaves the installation folder: ' + relative)
    return target

def load_bundle(root):
    manifest = json.loads((root / 'COMPLETE-INSTALL.json').read_text())
    if manifest.get('schema') != 1 or not manifest.get('files') or not manifest.get('skills'):
        raise ValueError('The complete installation manifest is missing or invalid. Download the package again.')
    if not re.fullmatch(r'[A-Za-z0-9_-]+', manifest.get('package','')) or any(not re.fullmatch(r'[a-z0-9-]+',s) for s in manifest['skills']):
        raise ValueError('Unsafe package or skill name in the installation manifest.')
    for rel, expected in manifest['files'].items():
        p = safe(root, rel)
        if not p.is_file() or digest(p) != expected:
            raise ValueError('Package check failed for ' + rel + '. Download and unzip the complete package again.')
    return manifest

def mapping(root, manifest, project, host):
    skillbase = project / ('.claude' if host == 'claude-code' else '.agents') / 'skills'
    package = project / '.operator-stack' / 'packages' / manifest['package']
    pairs = []
    for rel in manifest['files']:
        target = skillbase / rel[len('skills/'):] if rel.startswith('skills/') else package / rel
        if target.is_symlink() or any(p.is_symlink() for p in target.parents):
            raise ValueError('Installation destination contains a symbolic link. Choose an ordinary project folder.')
        pairs.append((safe(root, rel), target, manifest['files'][rel]))
    return pairs, skillbase, package

def verify(root, project, host, manifest):
    pairs, skillbase, package = mapping(root, manifest, project, host)
    missing, changed = [], []
    for source, target, expected in pairs:
        rel = str(source.relative_to(root))
        if not target.is_file(): missing.append(rel)
        elif digest(target) != expected: changed.append(rel)
    report = {'schema': 1, 'package': manifest['package'], 'release': manifest['release'],
        'host': host, 'expectedFiles': len(pairs), 'checkedFiles': len(pairs)-len(missing)-len(changed),
        'skills': manifest['skills'], 'missing': missing, 'changed': changed,
        'filesVerified': not missing and not changed,
        'aiSessionCheck': 'not-yet-confirmed', 'interview': 'not-yet-confirmed'}
    return report

def install(root, project, host, manifest, upgrade=False):
    pairs, skillbase, package = mapping(root, manifest, project, host)
    conflicts = [str(dst.relative_to(project)) for _, dst, expected in pairs if dst.exists() and (not dst.is_file() or digest(dst) != expected)]
    # A skill may contain personal extra files. Do not merge a new vendor version into it silently.
    expected_skills = {str(dst) for _,dst,_ in pairs if dst.is_relative_to(skillbase)}
    extras = []
    for name in manifest['skills']:
        folder = skillbase / name
        if folder.exists():
            for p in folder.rglob('*'):
                if p.is_symlink(): raise ValueError('A skill contains a symbolic link; resolve it before installation.')
                if p.is_file() and str(p) not in expected_skills: extras.append(str(p.relative_to(project)))
    if (conflicts or extras) and not upgrade:
        raise ValueError('Existing files differ; nothing was changed. Review these paths, then use --upgrade to back them up before replacing this package: ' + ', '.join((conflicts + extras)[:20]))
    project.mkdir(parents=True, exist_ok=True)
    backup = project / '.operator-stack' / 'backups' / uuid.uuid4().hex
    created, saved = [], []
    try:
        # Back up every changed file and removed extra. If any write fails, restore the previous state.
        for rel in dict.fromkeys(conflicts + extras):
            old = project / rel
            if not old.is_file(): raise ValueError('A directory occupies a file path: ' + rel)
            dest = backup / rel; dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(old, dest); saved.append((dest, old))
        for rel in extras: (project / rel).unlink()
        for source, target, expected in pairs:
            if target.is_file() and digest(target) == expected: continue
            if not target.exists(): created.append(target)
            target.parent.mkdir(parents=True, exist_ok=True)
            fd, tmp = tempfile.mkstemp(prefix='.os-install-', dir=target.parent)
            try:
                with os.fdopen(fd,'wb') as f: f.write(source.read_bytes())
                os.replace(tmp,target)
            finally:
                if os.path.exists(tmp): os.unlink(tmp)
        report = verify(root, project, host, manifest)
        if not report['filesVerified']: raise ValueError('The final file check failed; restoring the previous installation.')
        # The human-readable map belongs beside product files, never in business memory.
        index = project / '.operator-stack' / 'INSTALLED.json'
        existing = json.loads(index.read_text()) if index.exists() else {}
        existing[manifest['package']] = {'release':manifest['release'], 'host':host, 'skills':manifest['skills']}
        index.write_text(json.dumps(existing,indent=2)+'\n')
        report['backupCreated'] = bool(saved)
        return report
    except Exception:
        for p in reversed(created):
            if p.is_file(): p.unlink()
        for stored, original in saved:
            original.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(stored,original)
        raise

def main():
    p = argparse.ArgumentParser(description='Install every purchased component into one project, then verify its files.')
    p.add_argument('--project', required=True, help='Your business project folder')
    p.add_argument('--host', choices=['codex','claude-code'], required=True)
    p.add_argument('--verify', action='store_true', help='Check the installed files without changing anything')
    p.add_argument('--upgrade', action='store_true', help='Back up changed vendor skills before replacing them; never changes business files')
    args = p.parse_args()
    root = Path(__file__).resolve().parent; project = Path(args.project).absolute()
    try:
        manifest = load_bundle(root)
        result = verify(root,project,args.host,manifest) if args.verify else install(root,project,args.host,manifest,args.upgrade)
        print(json.dumps(result,indent=2))
        if not result['filesVerified']: return 2
        print('\nAll package files checked. Open a NEW AI session in this project. Use the installed operator-start skill and the product-specific session check from your access page or START-HERE guide when you want to verify setup.\nYou can start a job now with the facts you have and complete the business interview when you want a fuller brief.')
        return 0
    except (ValueError, OSError, KeyError, json.JSONDecodeError) as e:
        print('INSTALLATION NOT CONFIRMED: '+str(e), file=sys.stderr); return 1

if __name__ == '__main__': sys.exit(main())
