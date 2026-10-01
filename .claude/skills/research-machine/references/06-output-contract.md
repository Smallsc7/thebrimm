# Output contract

What the packet must contain, in order, and the fields downstream systems block without.

## Order matters

Coverage goes first, never in an appendix. It is what stops a thin read being spent against, and a reader who sees it last has already formed conclusions.

## The packet

**1. Coverage.** Open with the **collection tier**, in one line, before anything else. It says which sources were reachable. It is deliberately not worded like `status`, which says whether the evidence was sufficient: a collector run can still be `partial`, and often is.

- `collection_tier: collector` when the `last30days` collector ran. Name the sources it actually reached.
- `collection_tier: method-only` when it did not, so collection came from the host's own web search and supplied files. Say so plainly and name what that excludes, normally TikTok comments, Instagram comments and X. A method-only run is a legitimate deliverable, and hiding which tier produced a packet is how someone spends money against a read they thought was broader than it was.

Then: sources searched. Sources that returned nothing usable. How many discussions and review pages were actually opened. Quotes kept. Time window. Whether own-buyer material existed. Overall confidence. Say plainly where it is thin.

**2. The desire map.** The primary output. Per the desire engine: each surviving desire in the market's words with a quote and link, its why-chain, hell and heaven as scenes, scope and urgency and staying power, intensity tier, demand proxy and trend or an explicit note that sizing was unavailable, and whether the product can honestly serve it. Then the ranked list, the desire to lead with, and the plateau plan.

**3. The phrase bank.** Verbatim buyer language, grouped: how they name the problem, how they describe the failed alternative, how they describe success, and the words they use for the category. This is what stops downstream copy inventing its own vocabulary.

Include a **not-found list** rather than a ban list. Absence from a sample is not proof of absence from the market, so the honest form is "not found in this corpus", stated with the corpus size, the sources searched and the time window, for example: "not found across 340 collected items from Reddit, YouTube comments and 3 review pages, Aug 8 to Sep 7". That tells a writer the word carries no evidence of buyer usage, which is useful, without claiming buyers never say it, which is unprovable from a sample.

Two exceptions worth keeping: technical or clinical terms that explain the product accurately belong in copy even when buyers never search for them, and words the business is legally required to use are not optional. The not-found list informs the writer, it does not overrule them.

**4. Avatars.** The smallest set that carries distinct purchase decisions, each in the bundled avatar schema (eighteen numbered fields plus the why-chain) (`references/08-avatar-schema.md`), each with an evidence status.

**5. Objections, mapped to what answers them.** Two columns that matter: the surface objection, and the real one underneath. Each mapped to the response type it needs (guarantee, proof object, mechanism explanation, FAQ, risk reversal). The surface objection is rarely the real one.

**6. Alternatives and competitor perception.** What buyers use instead, including doing nothing, which is usually the market leader. What competitors are known for and where they disappoint. What the market has been trained to expect, because that is what your ad is arguing against whether you address it or not.

**7. Gaps in the market.** Typed, because the type decides the fix: product gap, positioning gap, education gap, distribution gap, trust gap. A trust gap answered with a new feature is wasted work.

**8. The test matrix.** Ranked. Each cell carries the desire it is built on and its intensity tier, plus the concept fields below. One principal variable changes per cell. Every cell names what would prove it wrong. Rank by what the cell would teach, not by predicted return.

**9. Gaps and asks.** What is still unknown, what it would take to know it, and what it is worth. Anything labelled `[ASSUMPTION]` appears here with its cheapest test.

## Fields downstream systems require

Paid media does not consume prose. It blocks without these, and research is the only place they can come from:

- **Avatar**: trigger situation, failed alternative, dominant emotion, persona sentence
- **Desire**: desire family, core desire sentence, desired state, the why-chain, intensity tier
- **Awareness**: the stage, and the basis for it. The basis is the evidence, not the guess
- **Belief**: current belief, target belief, the shift stated as a sentence
- **Angle**: the angle family and the angle as a full sentence
- **Mechanism**: why the old way failed, what is different, why that difference produces the result, what the buyer must do
- **Proof**: proof path, the actual proof objects, the authority and its type
- **Positioning**: the differentiation, and what habit or competitor the product makes incomplete
- **Hook**: the promise, the prequalification signal, and the buyer language it is built from
- **Narrative**: the emotion arc
- **Compliance**: which claims are being asserted, flagged for the claims gate

Operational fields (budgets, IDs, versions, gates, lineage) are not research output. Do not invent them.

## Four sentences that must be writable

If these cannot be written from the packet, the research is not finished, whatever its length:

- **Persona**: this is for [specific buyer] who [trigger or circumstance], has already [failed alternative or current belief], and needs [proof or risk condition] before buying.
- **Angle**: the argument is that [belief shift] so this buyer can [outcome] without [main fear or failed alternative].
- **Offer**: the offer frames [product] as [value or risk reversal] because [reason this buyer acts now].
- **Hook promise**: the opening promises [specific relevance] through [copy, visual or audio], without overpromising or jumping to the product.

## What the packet never does

It does not write finished ads, pages, emails or scripts. It does not decide budgets. It does not assert a claim as approved. It hands over evidence and a ranked plan, and stops where the writing and the deciding start.

## Run status: full, partial, or blocked

The depth pass is the bar for a **full** run. It is not a precondition for producing output, because a market with little public conversation is a real situation and a silent failure is worse than a labelled thin one.

**Depth is depth, not one proxy for it.** The bar started as ten discussions and three opened review pages, and that failed in practice for two reasons: the large review estates refuse automated fetching, and a business's own reviews, tickets and cancellation reasons are better evidence than any public review page (this file's own collection engine says so). A packet built on two hundred sales-call transcripts was being forced to `partial` by a missing proxy. So `full` is reachable by four routes, and the packet says which one it used:

| Route | What clears it |
|---|---|
| `reviews` | 10 discussions and 3 review pages. The original bar. |
| `own-buyer` | 10 discussions and 20 own-buyer items (their reviews, tickets, refund or cancellation reasons, sales-call notes, survey answers). |
| `mixed` | 10 discussions, 1 review page and 10 own-buyer items. |
| `discussions-only` | 20 discussions, AND `review_estate_blocked` naming each review estate you tried and why it refused. |

The `discussions-only` route is the one that can be abused, so it costs double the discussion depth and it will not pass without the record of what you tried. Recording an estate you never attempted is a lie in the packet, and no validator can catch that; the honesty is yours.

Coverage therefore carries, as whole numbers: `discussions_opened`, `review_pages_opened`, `own_buyer_items`, and when the route needs it, `review_estate_blocked` as a list of `{source, reason}`. Name the route in `depth_route`. Every packet therefore carries exactly one status at the top of Coverage:

| Status | Means | What it may recommend |
|---|---|---|
| `full` | One of the four depth routes was cleared and at least one desire has own-buyer or multi-source corroboration. | A lead desire, with the ranking policy stated and the depth route named. |
| `partial` | Real evidence, below the depth bar, or key sources unavailable. | Candidate desires, explicitly ranked as hypotheses. It must NOT name a lead desire as settled. |
| `blocked` | No collection was possible, or the ground truth contradicts itself on a fact the run depends on. | Nothing. It reports what is missing and the cheapest way to get it. |

A `partial` packet is a legitimate deliverable. Downgrading honestly is a pass, not a failure.

**Stop rule.** Stop collecting when any of these is true: the depth bar is met and the last two sources returned nothing new; three consecutive searches produce only repeats of quotes already banked; or the caller's stated budget of time, calls or spend is reached. Record which rule fired. Endless collection is not thoroughness.

**The four sentences are conditional.** Where the contract asks for four writable sentences, write only those the evidence and the ground truth support. Where a sentence cannot be written honestly, write the gap and what would close it. Never manufacture a sentence to complete the set.

## The machine-readable packet

The packet ships twice: `PACKET.md` for people and `packet.json` for software. They are generated from the same findings and must not disagree.

`packet.json` carries `schema_version` (start at `1.0.0`), the run metadata below, and every finding with a stable `id`. Each desire, avatar, objection and test references the `source_id`s behind it, so a downstream system can trace any recommendation to its evidence without re-reading prose. Unknown values are `null` with a sibling `*_unknown_reason` string; they are never `0`, `""` or an invented placeholder, because a zero silently becomes a fact in the next system.

Also emit `sources.json`: one row per collected item with `source_id`, URL, platform, the exact query that found it, collection timestamp, and any deduplication decision. Quotes in the packet cite `source_id`, not bare URLs.

Validate before publishing, with the validator shipped alongside this skill:

```bash
python3 <research-machine skill folder>/scripts/validate_packet.py research/<market-slug>/<run folder>
```

It checks that every referenced `source_id` exists in `sources.json`, that every `[OBSERVED]` finding carries at least one, that every `[INFERRED]` names what it was inferred from, that every `[ASSUMPTION]` carries a test, that unknowns are `null` with a stated reason, and that a `full` run actually recommends something. It exits non-zero when the packet is not publishable.

**What a green result means.** It means the packet is well formed and every claim traces to a source row. It does NOT mean the sources support the claims, and it is not a quality score. A validator can check structure; only a reader can check whether the evidence says what the finding says it says. Never present a passing validation as evidence that research is complete or publishable.

**Write in three steps, so a failed run cannot be mistaken for a good one.** A run folder is immutable once finalised, which is why the status is decided before it is finalised, not after:

1. **Stage.** Build the run folder and write `PACKET.md`, `packet.json`, `sources.json` and `raw/` into it.
2. **Validate.** Run the validator against the staged folder.
3. **Finalise.** If it passes, leave the folder as it is and move `latest` to it. If it fails, set `status` to `blocked` with the reason in the staged files, finalise the folder anyway so the failed attempt is on the record, and leave `latest` where it was.

After step 3 the folder is never edited again. A later run is a new folder.

## Where the packet is written

One immutable folder per run:

```
research/<market-slug>/<UTC timestamp>-<short run id>/
    PACKET.md
    packet.json
    sources.json
    raw/
```

The timestamp is `YYYYMMDDTHHMMSSZ` and the run id is a short random suffix, so two runs on the same day, or two started in the same second, are very unlikely to collide. A suffix lowers the risk; it is not a guarantee, so create the folder exclusively and pick a new suffix if the name is already taken. Run folders are never overwritten or edited once finalised.

**These are host responsibilities.** This skill ships the method and the validator, not a writer process. The staging, exclusive creation and pointer move are done by whatever runs the skill. Where that cannot be guaranteed, say so in Coverage rather than implying an atomicity the host does not provide.

A `research/<market-slug>/latest` pointer is updated to the newest run **only after validation passes**. Comparisons between runs read two run folders; they never mutate either.
