# Operator Stack checkpoint: The BRIMM

Updated: 2026-10-01

Business: The BRIMM (Sallie Ogden), Greenville, SC. One business per project; this project is The BRIMM only.
Approved brief: BUSINESS-MEMORY.md version 1 (approved with corrections 2026-10-01).

## Status
- Installation: The Research Machine package files verified (install.py --verify, release 20260925-onboarding-v13, 37/37); Research practice task passed (local validator). Other Machines: not installed, practice tasks not run.
- Collector: last30days v3.26.0 installed as a project skill at .claude/skills/last30days (preflight: ready; sources reddit, youtube, hackernews, polymarket, github, grounding). Run it with Python 3.12 (`LAST30DAYS_PYTHON=python3.12`). TikTok, Instagram and X are off (need a ScrapeCreators key or X backend).
- Business interview: COMPLETE. All 20 core questions, the triggered follow-ups (spend with unknown CPA, list over 1,000 unmailed) and the full-intake fields are answered or recorded as UNKNOWN/OPEN.
- Artifacts: BUSINESS-MEMORY.md, CONSTRAINT-CARD.md (constraint: OWNED-CHANNEL), research/GROUND-TRUTH.md (derived from BUSINESS-MEMORY.md v1).
- Real-world use: none yet. Interview completion is not evidence of revenue or a working campaign.

## Unresolved questions
See the OPEN section of BUSINESS-MEMORY.md. The most decision-relevant ones:
1. Is the current $2,500/mo 1:1 client continuing?
2. Does "seven this month" include the free lamp-founder seat?
3. Founder Forum agreement: drafted and signed?

## Environment notes
- This cloud workspace's network policy blocks growwiththebrimm.com; research collection also needs the network to reach Reddit, YouTube and the web.
- Make yt-dlp persistent by adding `uv tool install yt-dlp` to the environment's setup script.
- These files live on branch claude/gifted-hopper-w0ylcw until merged into the default branch. New sessions start from the default branch.

## Exact next action
Start a fresh session in this project and ask research-machine to run with research/GROUND-TRUTH.md, using the decision line in it. In parallel this week: THE ONE MOVE on CONSTRAINT-CARD.md (Founder Forum invitation to the engaged Flodesk segment + personal Gmail to past clients and warm contacts, with a dedicated booking link).
