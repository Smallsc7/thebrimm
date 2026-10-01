---
name: research-machine
description: "AUTOMATED research run that returns a machine-ready packet. Fed a ground-truth block rather than interviewing anyone, so use it when the caller wants the research DONE rather than to be walked through it: a full research pass, a scheduled or quarterly re-read, a desire map, a plateau diagnosis (has the desire pool saturated), or the buyer fields a downstream system blocks without. Collects across Reddit, X, YouTube, TikTok, Instagram, Hacker News, web and search-demand sources, then applies the mass-desire and Core Five avatar methods. Returns desires ranked by intensity with a demand proxy, avatars in the bundled avatar schema (eighteen numbered fields plus the why-chain), objections mapped to the proof each needs, a verbatim phrase bank, and a ranked test matrix, every finding labelled. For a guided, human-paced walkthrough with an interview and an approved plan, use the free Market Read instead if you have it; for a 30-day recency sweep, run the last30days collector alone. Writes no ads, pages or emails."
---
# The Research Machine

Feed it what is true about a business. It goes and finds what is true about the market, then returns the packet every downstream machine needs before it can do good work.

It is fed, not asked. With no approved brief, fill the ground-truth block from what the user gives you, write `unknown` for the rest, flag the missing facts, offer the operator-start interview once, and run with product-side statements labelled `[ASSUMPTION]`.

## What this is, and what it is not

| | Owner |
|---|---|
| Getting the business's own facts | The intake: a guided interview. Not this skill. |
| A guided, human-paced market walkthrough | The Market Read (free, separate), if installed. Not this skill. |
| **The automated deep research run that produces the machine-ready packet** | **This skill.** |
| Writing the ads, pages, emails | The Copy Machine (in the Full Stack beside this folder) |
| Deciding what to spend | The Meta and Google Ads Machines |

One method for every business. There is no service branch, agency branch or ecommerce branch. What changes between businesses is which sources hold evidence, never the method. A business with no customers runs the same sequence and gets more `[ASSUMPTION]` labels and a longer test list, which is the honest output for that situation.

## The run

0. **Preflight: can this session reach the market at all?** Before accepting a ground-truth block, establish how collection will happen here, and say it in one line. Three cases:
   - The `last30days` collector is installed: collect with it.
   - No collector: collect with the tool's own web search at the method-only tier. Search with it, open the result pages, read them. Say in the first line that the collector is not installed and give the install (`/plugin marketplace add mvanhorn/last30days-skill`, then `/plugin install last30days`, in Claude Code; `npx skills add mvanhorn/last30days-skill -g` elsewhere), then continue.
   - No collector and no web search: **stop here, before the block.** This Machine ships for Claude Code and Codex, which have both; if you are somewhere that has neither, say that nothing can be collected here and stop. Do not accept the block and then discover this in step 2; a blocked run after twenty minutes of the operator's typing is the failure this step exists to prevent.

1. **Ground truth.** Load the business facts. Do not research the business itself; that time belongs to the market. Contract: `references/01-ground-truth-contract.md`.
2. **Collect.** Run the collection engine across the sources that exist for this market. Rules, search craft and the known failure modes: `references/02-collection-engine.md`.
3. **Desire.** Find the desires the product can honestly serve, rank them, and pick the one to lead with. This is the spine of the output: `references/03-desire-engine.md`.
4. **Avatar.** Build the smallest set of avatars that carry distinct purchase decisions: `references/04-avatar-engine.md`, against the bundled schema in `references/08-avatar-schema.md`.
5. **Label.** Every finding gets an evidence label as it is written, not afterwards: `references/05-evidence-standard.md`.
6. **Package.** Emit the packet in the exact fields downstream systems require: `references/06-output-contract.md`.
7. **Declare the gaps.** Close by naming what is still unknown and the cheapest way to find out. A packet that says "I still need X" is worth more than one that pretends.

For unattended and repeat runs, including cadence and what a re-run may overwrite: `references/07-automation.md`.

## Rules that hold across every step

**Collect, then decide.** Do not form the conclusion first and go looking for support. The order is evidence, then reading of the evidence, then recommendation, and the output keeps those three visibly separate.

**A quote is evidence. Your reading of it is interpretation.** One quote proves a phrase was used. It never proves how common it is. No percentages from qualitative themes without a counted sample; "recurring theme" is the honest label.

**Never invent.** No invented facts, prices, specifications, credentials, testimonials, customer quotes, statistics or market sizes. A missing fact is an ASK, not a guess. This is the one rule with no exceptions and no mode that lifts it.

**Engagement is not demand.** Upvotes, views and comment counts tell you a conversation is live and give you its language. They cannot size a market. Sizing comes from search-demand tools, and the two reads stay visibly separate.

**Behaviour outranks opinion.** What people bought, compared, returned, cancelled or recommended beats what they said they would do. Opinions become copy language. Behaviour judges market reality.

**Say when it is thin.** A read that hides its own shallowness is worse than no read, because someone spends money against it. Coverage goes at the top of the output, never in an appendix.

**Research that changes nothing is hoarding.** Every section must be able to name the decision it changes: an angle, a hook, an offer, an objection to answer, a page section, or a test to run. If it changes none of those, cut it.

## Where the output goes

The packet is written to a durable, immutable run folder so the next session starts loaded rather than re-deriving, and so two runs never collide: `research/<market-slug>/<YYYYMMDDTHHMMSSZ>-<run id>/`, containing `PACKET.md`, `packet.json`, `sources.json` and `raw/`. A `latest` pointer is updated only after validation passes. Full contract: `references/06-output-contract.md`.

Downstream, the packet is the input to the Copy Machine, the Static Ads Machine, the Meta and Google Ads Machines and the Email Machine. Anything it marks `[ASSUMPTION]` is a test candidate, never a claim. Anything asserted as fact about a product, a result or a health outcome still passes the claims gate before it reaches a customer.

## Complete installation and business continuity

Use the installed operator-start skill for an installation check when asked, after an update, or when a required component is missing. **The buyer's current request comes first.** When they ask for a job, do that job now from what is available (the saved brief if there is one, the chat, and your best labeled assumption for the rest). List the brief facts that are missing in the flags and offer the business interview once, as one flag line. Never hold back the work to run the interview or an installation check first. Load this project's confirmed BUSINESS-MEMORY.md before asking for facts. Ask only missing or product-specific questions. Keep all requirements in this controller; the onboarding layer does not replace them. Locate supporting original files in the matching operator-resources skill under references/product on complete-bundle installations. Resume the saved business checkpoint on return. Never mix client projects or claim persistent memory without actual saved or attached files.
