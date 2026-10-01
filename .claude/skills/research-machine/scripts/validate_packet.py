#!/usr/bin/env python3
"""Validate a Research Machine run folder.

    python3 validate_packet.py research/us-home-massage/20260907T101500Z-a3f9

Exit 0 = publishable. Exit 1 = not publishable (reasons printed). Exit 2 = usage
or unreadable path.

What this can and cannot tell you. It checks STRUCTURE and TRACEABILITY: that the
files exist and parse, that every finding carries a stable id and an evidence
label, that every reference resolves to a real row in sources.json, that unknowns
say why they are unknown, and that a run claiming `full` actually cleared the
depth bar and has something to recommend. It CANNOT tell you that a source really
supports the claim attached to it. A green result means the packet is well formed
and traceable, never that the research is correct or complete. Read the evidence.

Dependency-free: standard library only, so it runs anywhere the collector runs.
"""

import json
import os
import re
import sys

SCHEMA_VERSION_RE = re.compile(r"^\d+\.\d+\.\d+$")
SUPPORTED_MAJORS = {1}
LABELS = {"OBSERVED", "INFERRED", "ASSUMPTION"}
STATUSES = {"full", "partial", "blocked"}
COLLECTION_TIERS = {"collector", "method-only"}
RUN_DIR_RE = re.compile(r"^\d{8}T\d{6}Z-[A-Za-z0-9]{3,}$")
SOURCE_FIELDS = ("url", "platform", "query", "collected_at")

# The depth pass, from references/06-output-contract.md. It is the bar for `full`
# only; a `partial` run below it is a legitimate deliverable.
#
# Depth is DEPTH, not one proxy for it. The first version of this gate required
# three opened review pages and nothing else would do, which failed in the real
# world for two reasons: the big review estates (Amazon, Walmart, G2, Capterra,
# Yelp) refuse automated fetching, and a business's own reviews, tickets and
# cancellation reasons are better evidence than any of them (this skill says so
# itself in 02-collection-engine.md). A packet built on 200 sales-call
# transcripts was being forced to `partial` by a missing proxy. So `full` is now
# reachable by four routes, and the packet records which one it used.
DEPTH_DISCUSSIONS = 10
DEPTH_REVIEW_PAGES = 3
DEPTH_OWN_BUYER = 20          # "Twenty of a business's own reviews... more than a thousand public comments"
DEPTH_MIXED_REVIEWS = 1
DEPTH_MIXED_OWN_BUYER = 10
DEPTH_DISCUSSIONS_ONLY = 20   # when the review estate is recorded as unreachable

DEPTH_ROUTES = ("reviews", "own-buyer", "mixed", "discussions-only")


def load(path, errors):
    if not os.path.isfile(path):
        errors.append(f"missing file: {os.path.basename(path)}")
        return None
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except json.JSONDecodeError as exc:
        errors.append(f"{os.path.basename(path)} is not valid JSON: {exc}")
    except OSError as exc:
        errors.append(f"cannot read {os.path.basename(path)}: {exc}")
    return None


def is_text(value):
    return isinstance(value, str) and value.strip() != ""


def as_int(value):
    return value if isinstance(value, int) and not isinstance(value, bool) else None


def ref_list(node, *keys):
    """Source references from any of `keys`, tolerating a bare string."""
    for key in keys:
        raw = node.get(key)
        if raw is None:
            continue
        if isinstance(raw, str):
            return [raw]
        if isinstance(raw, list):
            return raw
        return None  # present but the wrong type
    return []


def walk_labelled(node, path="packet"):
    """Every dict carrying an evidence label, wherever it sits in the packet."""
    if isinstance(node, dict):
        if "label" in node or "evidence_label" in node:
            yield path, node
        for key, value in node.items():
            yield from walk_labelled(value, f"{path}.{key}")
    elif isinstance(node, list):
        for i, value in enumerate(node):
            yield from walk_labelled(value, f"{path}[{i}]")


def check_unknowns(node, errors, path="packet"):
    """A null value must say why. A silent null becomes a fact in the next system."""
    if isinstance(node, dict):
        for key, value in node.items():
            if value is None:
                reason = node.get(f"{key}_unknown_reason")
                if not is_text(reason):
                    errors.append(
                        f"{path}.{key} is null with no {key}_unknown_reason "
                        f"(say why it is unknown, never leave it bare)"
                    )
            check_unknowns(value, errors, f"{path}.{key}")
    elif isinstance(node, list):
        for i, value in enumerate(node):
            check_unknowns(value, errors, f"{path}[{i}]")


def validate(run_dir):
    errors, warnings = [], []

    if not os.path.isdir(run_dir):
        print(f"not a directory: {run_dir}", file=sys.stderr)
        return 2

    base = os.path.basename(run_dir.rstrip("/"))
    if not RUN_DIR_RE.match(base):
        warnings.append(
            f"run folder '{base}' is not <YYYYMMDDTHHMMSSZ>-<run id>; same-day runs may collide"
        )

    packet = load(os.path.join(run_dir, "packet.json"), errors)
    sources = load(os.path.join(run_dir, "sources.json"), errors)

    # ---- the human-readable half must exist and say something
    md_path = os.path.join(run_dir, "PACKET.md")
    if not os.path.isfile(md_path):
        errors.append("missing file: PACKET.md (the packet must also be readable by a person)")
    else:
        try:
            if not open(md_path, encoding="utf-8").read().strip():
                errors.append("PACKET.md is empty; a packet nobody can read is not a deliverable")
        except OSError as exc:
            errors.append(f"cannot read PACKET.md: {exc}")

    # ---- raw evidence must be kept, on every tier
    raw_dir = os.path.join(run_dir, "raw")
    if not os.path.isdir(raw_dir):
        errors.append("missing folder: raw/ (collected evidence is kept, not summarised away)")
    elif not any(
        os.path.isfile(os.path.join(dirpath, f))
        for dirpath, _dirs, files in os.walk(raw_dir)
        for f in files
    ):
        errors.append("raw/ is empty; keep what was collected so a claim can be re-read")

    if packet is None or sources is None:
        for e in errors:
            print(f"FAIL  {e}")
        print(f"\nINVALID: {len(errors)} error(s).")
        return 1

    if not isinstance(packet, dict):
        print(f"FAIL  packet.json must be a JSON object, got {type(packet).__name__}")
        print("\nINVALID: 1 error(s).")
        return 1

    # ---- schema version
    sv = packet.get("schema_version")
    if not is_text(sv):
        errors.append("packet.json has no schema_version")
    elif not SCHEMA_VERSION_RE.match(sv):
        errors.append(f"schema_version '{sv}' is not semver")
    elif int(sv.split(".")[0]) not in SUPPORTED_MAJORS:
        errors.append(
            f"schema_version '{sv}' is not supported by this validator "
            f"(major version must be one of {sorted(SUPPORTED_MAJORS)})"
        )

    # ---- run block
    run = packet.get("run")
    if run is None:
        run = {}
    elif not isinstance(run, dict):
        errors.append(f"packet.run must be an object, got {type(run).__name__}")
        run = {}

    status = run.get("status") or packet.get("status")
    if status not in STATUSES:
        errors.append(f"run status must be one of {sorted(STATUSES)}, got {status!r}")

    # `collection_tier` says whether the collector ran. It is deliberately NOT
    # named with the same words as `status`, which says whether the evidence was
    # sufficient. A collector run can still be partial, and often is.
    tier = run.get("collection_tier") or run.get("tier")
    if tier is None:
        warnings.append(
            "run.collection_tier is not set; say 'collector' or 'method-only' so a reader "
            "knows which sources were reachable"
        )
    elif tier not in COLLECTION_TIERS:
        errors.append(
            f"run.collection_tier must be one of {sorted(COLLECTION_TIERS)}, got {tier!r}"
        )

    # ---- source index
    if isinstance(sources, list):
        rows = sources
    elif isinstance(sources, dict):
        rows = sources.get("sources", [])
    else:
        errors.append(f"sources.json must be a list or an object with a 'sources' list, got {type(sources).__name__}")
        rows = []
    if not isinstance(rows, list):
        errors.append("sources.json 'sources' must be a list")
        rows = []

    ids, dupes = set(), set()
    for i, row in enumerate(rows):
        if not isinstance(row, dict):
            errors.append(f"sources[{i}] is not an object")
            continue
        sid = row.get("source_id")
        if not is_text(sid):
            errors.append(f"sources[{i}] has no usable source_id (a non-empty string)")
            continue
        if sid in ids:
            dupes.add(sid)
        ids.add(sid)
        for field in SOURCE_FIELDS:
            if not is_text(row.get(field)):
                errors.append(
                    f"source {sid} has no {field}; a quote nobody can trace back is not evidence"
                )
    for sid in sorted(dupes):
        errors.append(f"duplicate source_id: {sid}")

    # ---- findings
    n_obs = n_inf = n_assume = 0
    corroborated = False
    seen_ids = {}

    declared = packet.get("findings")
    if declared is not None and not isinstance(declared, list):
        errors.append(f"packet.findings must be a list, got {type(declared).__name__}")
        declared = None

    entries = []
    if isinstance(declared, list):
        for i, node in enumerate(declared):
            if not isinstance(node, dict):
                errors.append(f"packet.findings[{i}] is not an object")
                continue
            entries.append((f"packet.findings[{i}]", node, True))
    seen_nodes = {id(n) for _p, n, _d in entries}
    for where, node in walk_labelled(packet):
        if id(node) not in seen_nodes:
            entries.append((where, node, False))

    for where, node, declared_here in entries:
        label = node.get("label") or node.get("evidence_label")
        if label is None:
            # A claim in the findings list with no label is exactly the thing the
            # evidence standard exists to prevent, so it is an error, not a skip.
            errors.append(
                f"{where}: no evidence label; every finding is [OBSERVED], [INFERRED] or [ASSUMPTION]"
            )
            continue
        if label not in LABELS:
            errors.append(f"{where}: label {label!r} is not one of {sorted(LABELS)}")
            continue

        fid = node.get("id") or node.get("finding_id")
        if declared_here:
            if not is_text(fid):
                errors.append(f"{where}: no stable id; downstream systems reference findings by id")
            elif fid in seen_ids:
                errors.append(f"{where}: duplicate finding id '{fid}' (also at {seen_ids[fid]})")
            else:
                seen_ids[fid] = where

        refs = ref_list(node, "source_ids", "sources")
        if refs is None:
            errors.append(f"{where}: source_ids must be a string or a list")
            refs = []
        bad = [r for r in refs if not is_text(r) or r not in ids]
        for r in bad:
            errors.append(f"{where}: source_id {r!r} is not in sources.json")

        if label == "OBSERVED":
            n_obs += 1
            if not refs:
                errors.append(f"{where}: [OBSERVED] with no source_ids")
            elif not bad and len({r for r in refs}) > 1:
                corroborated = True
            if node.get("own_buyer") is True:
                corroborated = True
        elif label == "INFERRED":
            n_inf += 1
            if not (is_text(node.get("inferred_from")) or refs):
                errors.append(f"{where}: [INFERRED] must name what it was inferred from")
        elif label == "ASSUMPTION":
            n_assume += 1
            if not is_text(node.get("test")):
                errors.append(f"{where}: [ASSUMPTION] with no test that would resolve it")

    check_unknowns(packet, errors)

    # ---- what each status is allowed to claim
    recommends = packet.get("lead_desire") or packet.get("recommendation")

    if status == "full":
        if not ids:
            errors.append("status is 'full' but sources.json is empty")
        if not recommends:
            errors.append("status is 'full' but no lead_desire or recommendation is present")

        coverage = packet.get("coverage")
        if not isinstance(coverage, dict):
            errors.append(
                "status is 'full' but there is no coverage block recording what was actually read"
            )
        else:
            disc = as_int(coverage.get("discussions_opened"))
            revs = as_int(coverage.get("review_pages_opened"))
            own = as_int(coverage.get("own_buyer_items"))
            if own is None:
                own = 0
            blocked = coverage.get("review_estate_blocked")
            blocked_ok = (
                isinstance(blocked, list)
                and bool(blocked)
                and all(
                    isinstance(b, dict) and is_text(b.get("source")) and is_text(b.get("reason"))
                    for b in blocked
                )
            )
            if blocked is not None and not blocked_ok:
                errors.append(
                    "coverage.review_estate_blocked must be a non-empty list of "
                    "{source, reason} objects: name the estate you tried and why it failed"
                )

            if disc is None or revs is None:
                errors.append(
                    "status is 'full' but coverage does not record discussions_opened and "
                    "review_pages_opened as whole numbers"
                )
            else:
                satisfied = []
                if disc >= DEPTH_DISCUSSIONS and revs >= DEPTH_REVIEW_PAGES:
                    satisfied.append("reviews")
                if disc >= DEPTH_DISCUSSIONS and own >= DEPTH_OWN_BUYER:
                    satisfied.append("own-buyer")
                if disc >= DEPTH_DISCUSSIONS and revs >= DEPTH_MIXED_REVIEWS and own >= DEPTH_MIXED_OWN_BUYER:
                    satisfied.append("mixed")
                if disc >= DEPTH_DISCUSSIONS_ONLY and blocked_ok:
                    satisfied.append("discussions-only")

                if not satisfied:
                    errors.append(
                        f"status is 'full' but no depth route was cleared. This run has {disc} "
                        f"discussions, {revs} review pages and {own} own-buyer items. Any one of "
                        f"these clears it: "
                        f"[reviews] {DEPTH_DISCUSSIONS} discussions and {DEPTH_REVIEW_PAGES} review pages; "
                        f"[own-buyer] {DEPTH_DISCUSSIONS} discussions and {DEPTH_OWN_BUYER} own-buyer items; "
                        f"[mixed] {DEPTH_DISCUSSIONS} discussions, {DEPTH_MIXED_REVIEWS} review page and "
                        f"{DEPTH_MIXED_OWN_BUYER} own-buyer items; "
                        f"[discussions-only] {DEPTH_DISCUSSIONS_ONLY} discussions with "
                        f"coverage.review_estate_blocked naming each estate you tried and why it refused. "
                        f"Otherwise set status to 'partial' and rank the desires as hypotheses; a "
                        f"labelled thin read is a pass, not a failure"
                    )
                else:
                    declared = coverage.get("depth_route")
                    if declared is None:
                        warnings.append(
                            "coverage.depth_route is not set; say which route cleared the depth bar "
                            f"(this run clears: {', '.join(satisfied)}) so a reader knows what the "
                            f"'full' rests on"
                        )
                    elif declared not in DEPTH_ROUTES:
                        errors.append(
                            f"coverage.depth_route {declared!r} is not one of {list(DEPTH_ROUTES)}"
                        )
                    elif declared not in satisfied:
                        errors.append(
                            f"coverage.depth_route claims {declared!r} but this run does not clear "
                            f"that route (it clears: {', '.join(satisfied)})"
                        )
        if not n_obs:
            errors.append("status is 'full' but there is not one [OBSERVED] finding")
        elif not corroborated:
            errors.append(
                "status is 'full' but no finding is corroborated: 'full' needs at least one "
                "[OBSERVED] finding carrying two or more source_ids, or marked own_buyer"
            )

    if status == "blocked" and recommends:
        errors.append(
            "status is 'blocked' but the packet still recommends something; a blocked run "
            "reports what is missing and the cheapest way to get it, and nothing else"
        )

    if status == "partial" and packet.get("lead_desire"):
        warnings.append(
            "status is 'partial' but a lead_desire is named; it should be a ranked hypothesis"
        )

    for w in warnings:
        print(f"warn  {w}")
    for e in errors:
        print(f"FAIL  {e}")

    if errors:
        print(f"\nINVALID: {len(errors)} error(s), {len(warnings)} warning(s).")
        print("Write the run folder anyway, set status to 'blocked', and do not move the 'latest' pointer.")
        return 1

    print(
        f"\nVALID (structure and traceability): status={status}, {len(ids)} sources, "
        f"{n_obs} observed, {n_inf} inferred, {n_assume} assumption(s), {len(warnings)} warning(s)."
    )
    print("This says the packet is well formed and every claim traces to a source. It does not")
    print("say the sources support the claims. Read the evidence before spending against it.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__.strip(), file=sys.stderr)
        sys.exit(2)
    sys.exit(validate(sys.argv[1]))
