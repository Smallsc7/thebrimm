# Automation

Running this unattended, on a schedule, and what a re-run is allowed to change.

## What can run without a human

The collection pass, the language extraction, the objection and alternative harvest, the demand sizing, and the coverage report are all mechanical enough to run unattended. Given a filled ground-truth block and a market, the machine can produce a complete draft packet with no input.

Two things should not be finalised unattended:

- **The lead desire decision.** The machine ranks and recommends. A person confirms, because gate 3 (can the product honestly satisfy this) depends on product knowledge the packet does not fully hold.
- **Anything headed for a customer.** The packet is research. Claims still pass their own gate before they reach an ad or a page.

An unattended run should therefore end at "here is the ranked map and the recommendation", not at "this is now the strategy".

## Setup is interactive. Execution is not.

These are two different phases and mixing them is what makes a "scheduled" run hang waiting for a human.

**Setup, once, with a person present.** The collector's own first run asks for consent: optional provider signup, optional CLI installs, optional cookie access. Those prompts are deliberate and must never be auto-accepted on someone's behalf. Do this before any schedule exists.

**Execution, unattended, never prompts.** A scheduled run must be able to complete with no input. That requires:

- `none` for own-buyer material is a valid, complete answer (Coverage records it as `own_buyer_evidence: none`). The method asks once, accepts `none`, records the absence in Coverage, and proceeds. It must not stall waiting for reviews that do not exist.
- Any `unknown` in the ground truth is a recorded gap, not a question that blocks the run.
- A missing optional source (no X backend, no ScrapeCreators key, no demand tool) lowers Coverage and may lower the run status to `partial`. It never pauses the run and never triggers a setup prompt.
- If a run would need consent it does not have, it finishes with status `blocked` and names exactly what was missing. Ending honestly beats waiting forever.

**Nothing in this package schedules anything.** There is no daemon, worker or timer here. A cadence is a recommendation to a human or to the host's own scheduler. A skill does not wake itself up, and this file recommending "quarterly" does not make quarterly happen.

## A scheduled run

Give it: the ground-truth block, the market, the topic list, and the output path. It returns the packet plus raw evidence.

Sensible cadence:

- **Quarterly** as a baseline. Markets move and packets rot. A packet older than a quarter should be treated as dated context, not current evidence.
- **On any pivot**: new market, new country, new product, new price band, or a change in who the buyer is.
- **On a plateau**: when a winning angle stops scaling, re-run to test whether the desire pool saturated or the market moved. This is the highest-value trigger, because it answers a question that costs money every day it stays open.
- **Not weekly.** A 30-day window re-read every week mostly re-reads itself, burns budget and produces the illusion of new information.

## Re-runs and what they may overwrite

A re-run is additive by default.

- **Never silently overwrite** a previous packet. Write a new dated file and keep the old one. The comparison between them is often more useful than either alone.
- **Carry forward** what has not changed, and mark what has: a desire that dropped out of the conversation, an objection that stopped appearing, a competitor that changed its story, new language that entered the market.
- **Upgrade labels honestly.** When something previously `[ASSUMPTION]` gets evidence, upgrade it and cite the source. When something previously `[OBSERVED]` has gone stale, downgrade it to dated rather than deleting it.
- **Keep the raw evidence.** Findings are re-readable only if the underlying rows survive.

## Cost discipline

Collection is the expensive part and most of it is wasted on breadth nobody reads.

- Narrow topics cost a fraction of broad ones and return more usable rows.
- Demand sizing is cheap per query and worth running on every candidate desire. It returns a demand proxy, not a pool size: it is the best available signal of relative direction between candidates, and it never becomes a buyer count without a stated model.
- Comment fetching is the expensive per-item call. Fetch comments for the threads that will actually be quoted, not for everything returned.
- If a source returns nothing twice on well-formed queries, stop paying it for that market and record the absence in Coverage.

## Failure handling

- **A source returns nothing**: record it in Coverage as unavailable. Do not treat silence as evidence that the market is quiet. Do not backfill the gap with inference and leave it unlabelled.
- **A run returns thin evidence overall**: say so at the top and produce the short honest packet. Do not pad it to look thorough. A thin packet that admits it is thin costs nothing; a padded one costs whatever gets spent against it.
- **The ground truth was incomplete**: name which fields were missing and what that made unreliable, rather than inferring the product.

## Portability

Nothing in this skill depends on a particular company, project layout, tool subscription or file tree. The business-specific facts live in the ground-truth block, and the output path is a caller argument.

The collection engine degrades rather than breaks: with no keys at all it still reaches Reddit, Hacker News, YouTube, GitHub and several others, which is enough for a real read in most consumer and prosumer markets. Paid sources widen coverage; they are not required for the method to run. When a source is unavailable, that belongs in Coverage as a stated limit, not as a silent gap.
