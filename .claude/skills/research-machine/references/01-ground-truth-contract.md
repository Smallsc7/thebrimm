# Ground truth contract

What the machine must be fed before it runs, and the format to feed it in.

## Why this exists

Most AI research is bad because the model is made to guess the business it is researching for. It burns half its effort inventing your product and your prices, and the half it spends on the market is contaminated by those inventions. Feeding ground truth first is the single highest-leverage thing a caller does. It also removes the largest source of fabricated output, because a model that has been told the facts does not need to manufacture them.

## The block

Paste this at the top of the run, filled in. It goes in unchanged on every re-run.

```
=== GROUND TRUTH: THE BUSINESS THIS RESEARCH IS FOR ===

Do not research this business. These are its facts, so you never guess them and spend
all of your effort on the market instead. Do not repeat these facts back to me.

WHAT IS SOLD
  Product or service, described plainly:
  What it physically is or mechanically does:
  What it does NOT do (be honest; this prevents wasted angles):
  Price points and how people pay:
  How it is delivered or fulfilled:

THE MARKET
  Where buyers are, and the language they buy in:
  Stage: pre-launch / launched-early / selling / scaling / mature:
  Where sales come from today, roughly:

WHAT IS ALREADY BELIEVED ABOUT THE BUYER  (will be tested, not trusted)
  Who buys, in one sentence:
  What happens right before they start looking:
  What they have already tried that did not work:

PROOF THAT EXISTS AND CAN BE DEFENDED
  Real numbers, with their source:
  Reviews, testimonials, case studies, and where they live:
  Credentials, guarantees, real terms:

CONSTRAINTS
  Claims that must not be made (regulated category, platform rules, legal lines):
  Things this business would never say:
  Capacity, inventory, geography or seasonality limits:

THE DECISION THIS RESEARCH MUST CHANGE
  What is being decided, and by when:
=== END GROUND TRUTH ===
```

## Rules for filling it

Two values are always valid and always complete: `unknown` where you do not know, and `none` where the thing genuinely does not exist (no customers yet, no reviews, no ad account, no sales channel). `none` is an answer, not a blank: the run proceeds, records the absence in Coverage, and never stops to ask again. This is what allows a scheduled run to complete without a human present.

Write `unknown` where it is unknown. Never guess a field to make the block look complete. Every `unknown` becomes a research job or an ASK, and that is useful information rather than a gap to be embarrassed about.

`What it does NOT do` earns its place. It is the field that prevents the machine building a desire the product cannot honestly serve, which is the most expensive research failure available.

`The decision this research must change` is not optional. A run without a named decision produces a document nobody acts on.

## If there is no ground truth yet

The operator-start interview is the best source: a guided interview that produces the business's own facts. Offer it once as a flag, but never hold the run for it. Without it, fill the block from what the user gives you, write `unknown` for the rest, and say plainly at the top of the packet that the business facts were unverified, and label every product-side statement `[ASSUMPTION]`. Do not quietly infer a product from its category.

## A note on pre-launch and zero-data businesses

A business with no customers, no reviews and no ad account is not blocked here. It runs the same sequence. The differences are honest ones:

- Own-buyer evidence is empty, so the market layer carries the whole read and the packet says so in Coverage.
- Proof comes from what the founder actually brings: credentials, prior results, existing audience, distribution already in hand, capital and hours available. Capture these in the proof section rather than leaving proof blank.
- More findings land as `[ASSUMPTION]`. That is the correct label, not a failure. Each one is written as a testable statement with the cheapest way to test it, so the packet doubles as a validation plan.
- The competitor's buyers stand in for your buyers. Their reviews, complaints and objections are the closest available evidence, and the packet labels them as what they are: evidence about a competitor's customers, not yours.
