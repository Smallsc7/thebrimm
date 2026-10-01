# What it reads, and what your install door can reach

The Research Machine comes in two halves.

```
the collector        goes and gets the raw material (Reddit, YouTube comments, TikTok, Instagram...)
the research skill   decides what to look for, what it means, and what to do about it
```

The skill is the method; the collector is a separate program that widens its reach. Both run in
Claude Code or Codex. That is the whole difference between the two tiers below, and the packet always
names its tier at the top of Coverage so you are never misled about which one you got.

**Two words that look alike and are not.** The **tier** (`collector` or `method-only`) says which
sources were reachable. The **status** (`full`, `partial` or `blocked`) says whether the evidence
that came back was enough to name a lead desire. A `collector` run can still be `partial`, and
often is: reaching every source does not mean the market said enough. Coverage prints both.

## The sources, in the order they matter

**Reddit.** Public, keyless, on by default. The single most valuable source for buyer language:
the problem in their words, the failed alternative, the comparison, the complaint, the
recommendation request, the aftermath. Every tier reads Reddit.

**Review pages, forums and the open web.** Three-star reviews name the exact trade-off a buyer
accepted; five-star reviews name the desire that pulled the purchase.

One thing worth knowing before you run it: **the big review sites refuse to be read by software.**
Amazon, Walmart, G2, Capterra and Yelp all block it, by design and permanently. Trustpilot is the
exception the collector has a direct line to, which covers consumer services, marketplaces, travel
and insurance. So if reviews matter for your market, **the best source is your own export**: your
Google reviews, your Amazon seller reviews, your support tickets, your cancellation reasons. Paste
them in. They are reachable, they are yours, and they beat the public estate anyway.

**Hacker News.** Always on, keyless. Matters for software and technical buyers.

**YouTube and its comments.** Free, keyless, one of the better sources of unfiltered buyer
language. Deep mode only; needs `yt-dlp` on your machine.

**TikTok and Instagram comments.** Where the buying language lives for most physical consumer
products. Deep mode only; needs a free ScrapeCreators key, which the collector offers to set up on
its first run. No card.

**X.** Optional. Deep mode only, and only with a paid API key. It is one source out of many and the
run is good without it; do not let it be the thing that stops you starting.

**Search demand.** Used for sizing, never engagement counts: a comment count says a conversation
is live, it cannot size a market. Deep mode with a free Brave key, or on Claude Code its own search.

**Your own material outranks all of it.** Twenty of your reviews, tickets or cancellation reasons
change the packet more than a thousand public comments. Paste them in.

That is not a slogan; the packet counts them. Twenty of your own items plus ten opened discussions clear
the depth bar, so a business with real customer material can reach a `full` read without opening a
public review page. For high-ticket B2B with no public reviews this is usually the best route; twenty
discussions with the blocked review sites recorded is the other.

## With the collector, and without it

Both run in Claude Code or Codex. The difference is reach, and the packet names which it had at
the top of Coverage.

| | What you get |
|---|---|
| **With the collector** (`collection_tier: collector`) | The skill plus the collector: Reddit with comment trees, Hacker News, YouTube and comments, TikTok and Instagram with comments, X if you add a key, search demand. The read worth having. |
| **Without it** (`collection_tier: method-only`) | The same method on the tool's own web search and anything you paste in: Reddit threads, forums, review pages, competitor sites, news. No comment sections, no X. Coverage names every source that was unavailable. |

The collector takes a minute to install and it is the difference between a narrow run and a good one,
so install it. The method-only run exists so that a missing collector produces a labelled thin read
rather than a silent failure.

## Deep mode: installing the collector

The research-machine skill's `references/02-collection-engine.md` has the full detail. The steps:

- **Claude Code:** type `/plugin marketplace add mvanhorn/last30days-skill` into the chat box, then
  `/plugin install last30days`. Two lines, inside your session, and Claude Code keeps it updated.
- **Codex, Cursor, Copilot, Gemini CLI:** `npx skills add mvanhorn/last30days-skill -g` in a
  terminal. That is the path its authors publish for those hosts.

It needs Python 3.12 or newer. The first time you run any research the collector offers its own
setup: say yes to the free key (TikTok and Instagram comments) and yes to the free command line
tools (YouTube). That happens once, and it is the difference between a narrow run and a good one.

## What it refuses to do

Invent. No invented quotes, statistics, market sizes or sources. When a source is unavailable it is
recorded in Coverage as unavailable, never backfilled with a guess. When the evidence is thin the
packet says so at the top. Absent sources are a coverage fact, not a failure.
