# Research packet: standing desks, US

**Status: `partial`.** Real run, real sources, thin evidence. Published as a worked example of what the
machine does when a market does not hand over much, and of how that is supposed to be reported.

Run `b4c1`, 2026-09-07T07:05:01Z to 07:06:36Z. Every source below was actually collected. Nothing in
this packet is invented, and where something is unknown it says so instead of filling the space.

## 1. Coverage

| | |
|---|---|
| Collection tier | collector (keyless sources only) |
| Sources searched | Reddit, Hacker News |
| Sources that returned anything usable | Reddit only |
| Sources unavailable | TikTok, Instagram, X, YouTube, search demand |
| Why unavailable | The run was deliberately restricted to keyless sources so anyone can reproduce it for nothing |
| Queries run | 3 |
| Discussions opened | 0 |
| Review pages opened | 0 |
| Depth bar met | **no** (no depth route cleared; see the four routes in 06-output-contract.md) |
| Verbatim quotes banked | **0** |
| Own-buyer evidence | none |
| Window | 30 days |
| Confidence | low |

Two of the three queries failed, and how they failed is worth recording. "why I returned my standing
desk" matched Hacker News posts containing the word *standing* about architecture, Parquet and a Grok
CLI. That is the documented failure mode: when results come back as news and unrelated links, the query
is wrong, not the market. Reformulating to "standing desk wobble too much" returned three on-topic
Reddit threads. "standing desk not worth it regret" returned nothing.

The collector returned titles, URLs and dates but **no post bodies**, which is a known behaviour of the
free path. So no buyer language was captured, and that single fact is what caps this run at `partial`.

## 2. Desire map

Not produced. Three titles do not support a desire map, and producing one anyway is the exact failure
this method exists to prevent.

Two candidates were recorded so the next run has somewhere to start:

**d1. Choose without regretting it.** `[INFERRED]` from the wording of one post title, [s1]. One post is
not a desire. Intensity unknown: no body text or comments were collected, so felt urgency was never
observed. Demand proxy unknown: no search-demand provider was configured.

**d2. A desk that does not wobble.** `[ASSUMPTION]`. This came from the query wording, not from the
market, and it is listed here in order to be disproved. Test: re-run with bodies and comments enabled,
read ten threads and three review pages, and see whether wobble appears in buyer language at all.

## 3. Phrase bank

One fragment of genuinely observed buyer wording, from a post title:

> "having a harder time choosing than I expected" [s1]

No not-found list is asserted. A not-found list needs a corpus, and three titles is not a corpus.

## 4. Avatars

None built. The schema requires an evidence status and the depth fields, and this run captured neither.
An avatar here would be a guess in a template.

## 5 to 8. Objections, alternatives, gaps, test matrix

Not produced, for the same reason. Each would require evidence this run did not obtain.

## 9. Gaps and the next action

- **No post bodies or comments.** This is the blocking gap. Everything else follows from it.
- No own-buyer evidence existed for this example.
- No demand proxy: no search-demand provider was configured.
- Two of three queries returned nothing on-topic.

Cheapest next action: re-run with comment enrichment and a ScrapeCreators key, then open ten
r/StandingDesk threads by hand and bank verbatim language before ranking any desire.

## Sources

| id | date | source |
|---|---|---|
| s1 | 2026-08-24 | [Best adjustable desk? I'm having a harder time choosing than I expected](https://www.reddit.com/r/StandingDesk/comments/1vx0aha/best_adjustable_desk_im_having_a_harder_time/) |
| s2 | 2026-09-05 | [Trying to snag a Labor Day Weekend deal, recs/reviews for the Best 4 Legged Standing Desk for women](https://www.reddit.com/r/StandingDesk/comments/1w7p9f5/trying_to_snag_a_labor_day_weekend_deal_i_need/) |
| s3 | 2026-08-24 | [Picked up my Uplift standing desk for $200, any suggestions for accessories and monitor arms](https://www.reddit.com/r/StandingDesk/comments/1vwsmef/picked_up_my_uplift_standing_desk_for_200_any/) |

Raw collector output for both queries is in `raw/`.

## Why this example is worth shipping

A packet that says "I found three posts and no quotes, here is what that is worth" is more useful than
a confident one built on the same three posts. This run is what `partial` looks like, and it is the
output most first runs on a quiet market should produce.
