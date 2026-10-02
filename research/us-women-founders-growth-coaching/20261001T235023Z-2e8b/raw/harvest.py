"""Depth-pass harvester against the Arctic Shift Reddit archive.

Usage: python3 harvest.py <run_dir> search   -> raw/arctic-search.json (post candidates, with the query that found each)
       python3 harvest.py <run_dir> comments <id,id,...> -> raw/threads/<id>.json
"""
import json, os, sys, time, urllib.parse, urllib.request, datetime

BASE = "https://arctic-shift.photon-reddit.com/api"
FIELDS = "id,title,num_comments,score,created_utc,subreddit,author"


def get(path, params, tries=5):
    url = f"{BASE}/{path}?{urllib.parse.urlencode(params)}"
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "research-machine/1.0"}), timeout=60) as r:
                d = json.load(r)
            if d.get("error"):
                raise RuntimeError(d["error"])
            return d.get("data") or [], url
        except Exception as e:  # noqa
            time.sleep(6 * (i + 1))
            err = e
    print(f"  FAILED {url}: {err}", file=sys.stderr)
    return None, url


# (family, subreddit, field, term): single words, filtered locally afterwards
QUERIES = []
PLAN = {
    "smallbusiness": ["coach", "mastermind", "consultant", "agency", "overwhelmed", "burnout", "plateau", "stuck", "husband"],
    "Entrepreneur": ["coach", "mastermind", "consultant", "overwhelmed", "burnout", "plateau", "husband"],
    "femalefounders": ["coach", "mastermind", "consultant", "agency", "overwhelmed", "burnout", "stuck", "husband"],
    "EtsySellers": ["coach", "wholesale", "overwhelmed", "burnout", "stuck", "husband"],
    "jewelrymaking": ["business", "wholesale", "burnout"],
    "interiordesign_pros": ["business", "coach", "clients", "grow"],
}
FAM = {"coach": "coach", "mastermind": "mastermind", "consultant": "consultant", "agency": "agency",
       "overwhelmed": "maxed-out", "burnout": "maxed-out", "plateau": "plateau", "stuck": "plateau",
       "husband": "spouse", "wholesale": "wholesale", "business": "creative-owner", "clients": "creative-owner", "grow": "creative-owner"}
for sub, terms in PLAN.items():
    for t in terms:
        QUERIES.append((FAM[t], sub, "title", t))


def windows_split():
    # half-year windows from 2025-01-01 to now keep full-text queries under the archive timeout
    start = datetime.date(2025, 1, 1)
    end = datetime.date.today() + datetime.timedelta(days=1)
    cur = start
    while cur < end:
        nxt = min(datetime.date(cur.year + (cur.month + 5) // 12, (cur.month + 5) % 12 + 1, 1), end)
        yield cur.isoformat(), nxt.isoformat()
        cur = nxt


def windows():
    yield "2025-01-01", (datetime.date.today() + datetime.timedelta(days=1)).isoformat()


def search(run):
    ck = os.path.join(run, "raw", "arctic-search.json")
    out, seen, done = [], {}, set()
    if os.path.exists(ck):
        prev = json.load(open(ck))
        for p in prev["posts"]:
            p["families"] = set(p["families"]); seen[p["id"]] = p
        out = [dict(failed=f["failed"], family=f["family"]) for f in prev.get("failures", [])]
        done = set(tuple(q) for q in prev.get("done", []))
    for fam, sub, field, term in QUERIES:
        if (fam, sub, field, term) in done:
            continue
        for a, b in windows():
            params = {"subreddit": sub, field: term, "after": a, "before": b, "limit": 100, "fields": FIELDS, "sort": "desc"}
            data, url = get("posts/search", params)
            time.sleep(4)
            if data is None:
                sub_ok = True
                for a2, b2 in windows_split():
                    params2 = dict(params, after=a2, before=b2)
                    d2, u2 = get("posts/search", params2)
                    time.sleep(4)
                    if d2 is None:
                        out.append({"failed": u2, "family": fam}); sub_ok = False
                        continue
                    data = (data or []) + d2
                if data is None:
                    continue
            if False:
                out.append({"failed": url, "family": fam})
                continue
            for p in data:
                if p["id"] in seen:
                    seen[p["id"]]["families"].add(fam)
                    continue
                p["families"] = {fam}
                p["query"] = f"arctic-shift posts/search subreddit={sub} {field}=\"{term}\" after={a} before={b}"
                p["collected_at"] = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
                seen[p["id"]] = p
        done.add((fam, sub, field, term))
        snap = [dict(p, families=sorted(p["families"])) for p in seen.values()]
        json.dump({"posts": snap, "failures": out, "done": sorted(done)}, open(ck + ".tmp", "w"))
        os.replace(ck + ".tmp", ck)
        print(f"{fam:16} r/{sub:20} {term!r}: total {len(seen)}", file=sys.stderr)
    rows = []
    for p in seen.values():
        p["families"] = sorted(p["families"])
        rows.append(p)
    json.dump({"posts": rows, "failures": [o for o in out if "failed" in o], "done": sorted(done)}, open(ck, "w"), indent=1)
    print(f"{len(rows)} posts, {len(out)} failed requests", file=sys.stderr)


def flatten(nodes, acc, depth=0):
    for n in nodes:
        d = n.get("data", n)
        if d.get("body"):
            acc.append({"id": d.get("id"), "parent_id": d.get("parent_id"), "author": d.get("author"), "score": d.get("score"), "depth": depth, "body": d.get("body")})
        rep = d.get("replies")
        if isinstance(rep, dict):
            flatten(rep.get("data", {}).get("children", []), acc, depth + 1)
        elif isinstance(rep, list):
            flatten(rep, acc, depth + 1)


def comments(run, ids):
    os.makedirs(os.path.join(run, "raw", "threads"), exist_ok=True)
    for pid in ids:
        post, purl = get("posts/ids", {"ids": pid})
        tree, turl = get("comments/tree", {"link_id": pid, "limit": 400})
        acc = []
        flatten(tree or [], acc)
        rec = {"post": (post or [{}])[0], "post_url": purl, "tree_url": turl, "collected_at": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"), "comments": acc}
        json.dump(rec, open(os.path.join(run, "raw", "threads", f"{pid}.json"), "w"), indent=1)
        print(f"{pid}: {len(acc)} comments", file=sys.stderr)
        time.sleep(1.5)


if __name__ == "__main__":
    run = sys.argv[1]
    if sys.argv[2] == "search":
        search(run)
    else:
        comments(run, sys.argv[3].split(","))
