# Research packet: BLOCKED

**collection_tier: collector** (last30days installed and ran), **status: blocked**, because no market source was reachable from this workspace.

## Coverage
- **Searched:** Reddit, YouTube and Hacker News through the last30days collector (3 planned subqueries, 90-day window, subreddits smallbusiness, Entrepreneur, EtsySellers, InteriorDesign, sweatystartup, Etsy). Also the host web search as the fallback.
- **Returned usable:** nothing.
  - Reddit: the network proxy refused it (403).
  - Hacker News: authentication failed.
  - YouTube: no results.
  - Web search: titles and generated summaries only, with no pages opened, because page fetching is blocked by the environment's network policy.
- **Discussions opened:** 0. **Review pages opened:** 0. **Quotes kept:** 0.
- **Own-buyer material:** 1 prospect call (Prospect L.W., 24 Sept 2026), summarized in BUSINESS-MEMORY.md. It isn't re-analysed in a blocked run.
- **Confidence:** none. Nothing was collected.

## Why it is blocked
This cloud environment's network access setting blocks the sites research needs. This packet makes no recommendation and names no desire. It doesn't use the web search summary either, because that included a statistic with no source, which would be an invented number.

## What it needs, cheapest first
1. **Network access:** set this environment's network access to full, or allow reddit.com, youtube.com, googlevideo.com, hn.algolia.com and general web page fetching. Then start a new session.
2. **Setup:** add `uv tool install yt-dlp` to the setup script, and `LAST30DAYS_PYTHON=python3.12` as an environment variable.
3. **Optional:** the free ScrapeCreators key, for TikTok and Instagram comments.
4. **Own-buyer material, which works even without network:** more sales-call recordings or notes, testimonials, workshop feedback, and the reasons people said no. A handful of these outweighs hundreds of public posts.

The ground truth is ready at `research/GROUND-TRUTH.md`. The next run can start straight from it.
