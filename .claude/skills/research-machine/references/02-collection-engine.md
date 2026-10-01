# Collection engine

How to actually gather evidence, which sources to use, and the failure modes that waste a run.

## The engine

`last30days` is the breadth pass. It sweeps a 30-day window across Reddit, Hacker News, Polymarket, GitHub, YouTube, arXiv, Techmeme and Digg with no keys, and adds X, TikTok, Instagram, Threads, Pinterest, LinkedIn and web search where credentials exist. It returns dated items with URLs, vote counts and verbatim text, clustered and ranked by engagement.

Use it to find where the conversation is and what language it uses. Then go deeper by hand on what it surfaces.

### If the collector is not installed

`last30days` is a separate plugin and this skill does not ship it. Check before planning a run.

If it is missing, say so plainly and give the install line for the caller's host rather than quietly substituting a weaker pass:

- **Claude Code:** two slash commands, typed into the chat; the marketplace keeps it updated:

  ```
  /plugin marketplace add mvanhorn/last30days-skill
  /plugin install last30days
  ```

- **Codex, Cursor, Copilot, Gemini CLI:** the shared agent-skills installer, in a terminal:

  ```
  npx skills add mvanhorn/last30days-skill -g
  ```

It needs Python 3.12 or newer. Do not invent a host-specific plugin command; those two are the paths its authors publish.

Then continue at **method-only tier**: collection comes from the host's own **web search tool** (search with it, open the result pages with it), plus any files the caller supplies. Use the search tool, never a network call from a code sandbox, and never report a sandbox network failure as "the sources returned nothing". If there is no search tool either, the run is `blocked` before the block is read (SKILL.md, step 0). Do that work properly rather than apologising for it. Search inside platforms, open the threads, read the review pages: the mandatory depth pass still applies and native fetch is good at it.

What method-only cannot reach is the social sweep: TikTok comments, Instagram comments and X. Record the tier at the top of Coverage, name those exclusions, and let the run finish at `partial` if the evidence is thin. Never write the packet as though the full sweep happened.

This Machine ships for Claude Code and Codex only. Method-only is the fallback for a local session where the collector has not been installed yet; the fix is the two-line install, and the packet says so.

### What is active, and what that costs the run

Source availability varies by machine, so never assume a source ran. The collector's preflight reports what is actually on; invoke its engine directly: `python3 <collector folder>/scripts/last30days.py --preflight` (Python 3.12 or newer). Here, `<collector folder>` means the folder containing the installed last30days skill's own `SKILL.md` and `scripts/`, not the enclosing plugin or global skills folder. Read that installed skill's current setup instructions first; some plugin versions nest it under `skills/last30days/`. Preflight reads configuration to report it, does not read browser cookies, and does not prove any source will return results. Reddit, Hacker News and Polymarket need no keys at all. TikTok and Instagram, with their comments, need a free ScrapeCreators key that the plugin offers on first run. YouTube and its comments need `yt-dlp` on PATH and no key. X needs one of several backends and is the most likely to be absent.

Absent sources are a coverage fact, not a failure. Record them in Coverage by name. A desire map built without TikTok and Instagram on a consumer product is materially thinner than one with them, and the reader has to be able to see that.

### Operating rules, learned from real runs

These are not preferences. Each one comes from an observed failure.

1. **Narrow topics, run separately.** A broad multi-platform run returned 60 rows padded with off-topic content, and its planned subqueries never reached the social fetches; the same market split into narrow topics returned usable results in a fraction of the time. Run five or six specific topics rather than one broad one.
2. **Never use the quick path** for real work. It fires a subset of sources and will silently return Reddit only.
3. **Expect comment enrichment to come back empty.** Pick the highest-signal threads and fetch their comments separately. Original-post fields can return null; take post wording from the search or page evidence, not from the null field.
4. **Ignore the engine's own quality score.** A source reporting "ok" is not evidence it returned anything useful. Inspect the rows.
5. **Always run it with a plan. A bare invocation is the most common way to waste a run.** `python3 <collector folder>/scripts/last30days.py "<topic>" --deep` with nothing else lets the engine sweep every source it has, which returns padding from wherever it happens to look (Hacker News laptop threads, Digg, Polymarket sports markets) and can take half an hour a topic while it pulls transcripts from every video it finds. Write a plan first: a few subqueries, each with its own ranking sentence saying what a good row looks like and what to exclude, and `--search` (a comma-separated source list) pinned to the platforms this market actually uses. Then pass it with `--plan <file>`. Named entities and products need this most.

   A ranking sentence that works looks like: "Find firsthand complaints from people who bought one. Prefer explicit United States context; do not infer geography from English. Exclude brands promoting cures." The point is to tell the engine what to keep, not just what to search.

## Search craft

The engine finds threads. Craft finds the right ones.

**Search inside the platform, not around it.** General web search returns marketing articles and news. Build searches against each platform's own search. If results come back as SEO listicles, vendor pages or news, the query failed. That does not mean the market is quiet; it means the query was wrong. Reformulate before concluding anything.

**Triage by comment count, but only inside a scope you have already narrowed.** Sorting by comments across a whole platform surfaces whatever went viral that month, not what is true about your market. Narrow to a community or a precise topic first.

**Query families to run, not just the obvious one:**
- the problem in the buyer's words, not the category's words
- the failed alternative ("tried X, did not work")
- the comparison ("X vs Y", "is X worth it")
- the complaint ("X sucks", "problem with X")
- the recommendation request ("what should I buy for X")
- the aftermath ("I bought X, here is what happened")
- the adjacent pain, when the obvious pain is thin

**The depth pass is the bar for a `full` run.** Clear one of the four depth routes in `06-output-contract.md` (reviews, own-buyer, mixed, discussions-only). A read built only from search-result snippets is a summary of headlines, so below that bar the packet is `partial`: it still produces the pain map, the objection table and ranked candidate desires, and it must not name a lead desire as settled. Some markets have little public conversation, and a labelled thin read beats a silent one. Status definitions: `06-output-contract.md`.

**Read three-star reviews first.** One-star reviews are often about shipping and five-star reviews are often about nothing. Three-star reviewers thought about it and name the exact tradeoff they accepted, which is where objections and honest limits live.

**Read five-star reviews for the desire.** They tell you which desire actually pulled the purchase, which is different from what the objections tell you.

## Sizing is a different job with different tools

Engagement counts cannot size a market. When the packet needs pool size, direction or seasonality, use search-demand data (search volume, related terms, trend direction). Keep the two reads visibly separate in the output: one says a desire is live and gives its language, the other gives a demand proxy. Everything downstream calls this field the demand proxy, never pool size.

**Search volume is a proxy, not a headcount.** It counts queries, not people. One person searches the same thing repeatedly, related queries overlap and double-count, and identical wording can carry different intent. Never convert volume into a number of buyers or a market size without a stated model, and never present it as one. Every volume figure in the packet carries four things or it does not go in: the provider, the geography, the time window, and a one-line note on what it excludes. Write it as "demand proxy", not "pool size".

If no demand tool is available, say the sizing is unavailable rather than substituting engagement for it. An unsized desire is an honest gap. An engagement-sized desire is a wrong number that will get spent against.

## Where reviews actually live, and what will refuse you

The depth pass asks for review pages because three-star reviews carry the exact trade-off a buyer accepted, which discussions rarely state that plainly. Getting them is the hard part, and it is worth knowing before you plan the run rather than after.

**Assume the large review estates refuse automated fetching.** Amazon, Walmart, G2, Capterra and Yelp all answer a plain programmatic request with a block, a redirect or a challenge, and that is their steady-state behaviour rather than an outage. Do not record a block as "the source returned nothing": it is an unavailable source, and it belongs in `review_estate_blocked` with the reason.

**Trustpilot is the one with a dedicated route.** The collector takes `--trustpilot-domain <domain>`, which is a first-class source rather than a generic fetch. A host with a real browser can usually open Trustpilot pages too, where a plain fetch cannot. It covers consumer services, marketplaces, insurance, energy, telecoms, travel and home-services aggregators. It does not cover B2B software or a local trade.

**For most businesses the best review estate is their own.** A service business can export its own Google reviews; an ecommerce seller can export Amazon and Shopify reviews from the seller side; anyone with support tooling can export tickets and cancellation reasons. That material is reachable, it is theirs, and by the section below it outranks the public estate anyway. Ask for it before you plan a scrape around a wall.

**By business type, so you can plan before you collect:**

| The business | Where its reviews are | What to expect |
|---|---|---|
| Consumer product | Amazon, Walmart, retailer pages | Refuses fetching. Use the seller's own export, or a standing corpus. |
| Consumer service, marketplace, travel, insurance | Trustpilot | Reachable through the collector's own flag. The best case. |
| Local service (trades, clinics, gyms, restaurants) | Google Maps, Yelp | Effectively closed to a fetch. Their own Google review export is the route. |
| B2B software | G2, Capterra | Refuses fetching. Discussions carry more here anyway. |
| High-ticket B2B services | Nowhere public | The evidence does not exist publicly. Own-buyer material is the whole route: call recordings, lost-deal reasons, churn interviews. |

For the last two rows the discussion layer is unusually strong, which is why the `discussions-only` route exists. Use it honestly.

## Own-buyer evidence outranks everything public

Twenty of a business's own reviews, support tickets, refund reasons, cancellation reasons, sales-call notes or survey answers change the output more than a thousand public comments. Ask for them once. Accept "none" without pushing twice, and record the absence in Coverage.

Never request or retain names, emails, phone numbers, addresses or payment details. Quote what a customer said about the problem, never who they are.

## Coverage, recorded as you go

Track while collecting, not afterwards: sources searched, sources that returned nothing usable, discussions and reviews actually opened, quotes kept, the time window, whether own-buyer material existed, and overall confidence. This becomes the first section of the packet. It is what stops a thin read being spent against.
