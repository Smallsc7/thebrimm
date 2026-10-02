import json,sys,os,datetime
T=sys.argv[1]
for pid in sys.argv[2].split(','):
    r=json.load(open(f"{T}/{pid}.json")); p=r['post']
    dt=datetime.datetime.utcfromtimestamp(p.get('created_utc',0)).date()
    print(f"\n######## {pid} r/{p.get('subreddit')} {dt} [{p.get('score')}pts {p.get('num_comments')}c] {p.get('title')}")
    print("POST:", (p.get('selftext') or '')[:1500].replace('\n',' '))
    cs=[c for c in r['comments'] if c['author'] not in ('AutoModerator','[deleted]') and c['body'] not in ('[deleted]','[removed]')]
    cs.sort(key=lambda c:-(c['score'] or 0))
    for c in cs[:int(sys.argv[3]) if len(sys.argv)>3 else 14]:
        print(f"  - [{c['id']} u/{c['author']} {c['score']}] {c['body'][:450].replace(chr(10),' ')}")
