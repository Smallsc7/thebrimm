# Evidence standard

One vocabulary, applied to every finding, with a mapping for the others already in use.

## Why this file exists

Other Operator Stack skills (project-memory-manager, feed-the-machine, the avatar schema) use their own labels. This file fixes the Research Machine's vocabulary and gives the mapping so a packet can be consumed by skills that speak the others: `memory-derived` reads as `[OBSERVED]`, dated, to reverify; `source-claim` reads as `[OBSERVED]` that the source said it, not that it is true; `unavailable` is not a finding and is recorded in Coverage.

## The three labels

Every finding carries exactly one.

**`[OBSERVED]`**: you found it stated, and you can link it. The link is not optional. An observed finding without a source is not observed.

**`[INFERRED]`**: you concluded it from evidence you can link, but nobody said it. Name the evidence you inferred from. If you are writing a confident sentence with no link behind it, it is `[INFERRED]` at best.

**`[ASSUMPTION]`**: you are filling a gap to keep the read usable, and it needs testing. Every assumption in the packet carries the cheapest test that would resolve it, and what result would change the conclusion.

A finding without a label is not finished. A downstream summary may weaken a label, never upgrade one.

## Confidence, which is a separate axis

Labels say where a finding came from. Confidence says how much weight it carries.

- **High**: repeated across five or more independent sources or communities, specific, recent, from people who look like buyers.
- **Medium**: repeated, but concentrated in one community or one period.
- **Low**: one or two mentions, an isolated anecdote, a joke thread, or likely vendor content.

Low-confidence findings may stay in the packet. They must be labelled, and they must never carry a recommendation on their own.

## Mapping to the other vocabularies

When consuming or emitting for a system that uses a different set:

| Other vocabulary | Maps to | Note |
|---|---|---|
| `verified-current` | `[OBSERVED]` | Source is current at time of writing |
| `local-snapshot` | `[OBSERVED]`, dated | Carry the date; it decays |
| `inference` | `[INFERRED]` | Direct equivalent |
| `assumption` | `[ASSUMPTION]` | Direct equivalent |
| `validated` (avatar schema) | `[OBSERVED]` with a cited source | Never assert without the citation |
| `hypothesis` (avatar schema) | `[INFERRED]` or `[ASSUMPTION]` | Choose by whether evidence exists to infer from |
| `repeated qualitative signal` | `[OBSERVED]`, confidence Medium or High | Repetition raises confidence, not the label |
| `single-source hypothesis` | `[INFERRED]`, confidence Low | |
| `needs research` | `[ASSUMPTION]` with the test named | |

Claim risk is a different axis again and is not an evidence label. Whether something is legally sayable is decided downstream by the claims gate, not here. A finding can be `[OBSERVED]` with high confidence and still be unusable in an ad.

## Hard rules

**Separate what people said from what you concluded.** A quote is evidence. Your reading of it is interpretation. The packet keeps them in different sentences.

**One quote proves a phrase was used.** It never proves how common it is. No percentages from qualitative themes without a counted sample. "Recurring theme" is the honest label; "68% of buyers say" without a survey is a fabrication.

**Never flatten several people into one composite quote.** If three reviewers said similar things, quote one and note the repetition. A stitched quote is an invented customer.

**Distinguish a repeated signal from a single loud response.** Volume of words is not volume of people.

**English-language sources do not establish geography.** If the market matters, say what the evidence can and cannot establish about where these people are.

**Own-buyer evidence is purchaser-conditioned.** Reviews and post-purchase surveys tell you why people who bought, bought. They do not explain why qualified people did not, and they do not establish market prevalence.
