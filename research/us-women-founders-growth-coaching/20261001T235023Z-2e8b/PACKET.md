# Research packet: Founder Forum market read

Run `20261001T235023Z-2e8b`, 2026-10-02. Built for The BRIMM's decision: who to prioritise, what message makes Founder Forum worth acting on now, and which channels to use for 7 members by October 14 and about 26 by mid-December. Replaces the blocked run `20261001T220852Z-2997`.

Every claim carries a source ID (R = Reddit, T = Trustpilot, G = Google autocomplete, OB1 = the one prospect call, GT1 = the ground truth). The quotes are in `sources.json`. The machine-readable copy is `packet.json`.

---

## 1. Coverage (read this first)

**collection_tier: collector.** The last30days collector ran and reached Reddit, YouTube and Hacker News. Reddit blocks this host directly, so the depth pass went through the Arctic Shift Reddit archive.

**status: full**, depth route `discussions-only`, **confidence: medium.**

| | |
|---|---|
| Discussions opened and read | 36 threads, 2,473 posts and comments |
| Candidate posts harvested | 1,743 from 37 archive queries (6 requests failed) |
| Review pages opened | 4 Trustpilot pages with reviews (ActionCOACH, Hello Seven, Female Entrepreneur Association, Tony Robbins). The fetch tool returns a summary, not raw text, so none of it is used as buyer language. |
| Review estate refused or empty | G2, Capterra, Yelp (403); Vistage and Strategic Coach have 0 Trustpilot reviews; Business Made Simple and EntreLeadership have no page; YouTube comments bot-gated |
| Own-buyer evidence | 1 prospect call (L.W., jewelry, Sept 24). Prospect, not customer, and not for marketing use. |
| Quotes kept | 52 |
| Window | Reddit Jan 2025 to Oct 2026 (about 21 months, because this conversation is low-volume); collector July to October 2026 |
| Not reached | X, TikTok, Instagram (no credentials); search volume (Google Trends refused); interior-designer pro communities (no results) |
| Excluded | Two coaching threads astroturfed by one coaching firm (other commenters call it out, R10), and one disguised ad (R51) |

**Where it is thin:**
- **Gender.** Most posters don't say. Women-specific evidence is three r/Femalefounders posts plus the prospect call. That the buyer is a woman comes from the ground truth, not from this corpus.
- **Geography.** English doesn't establish the US.
- **Creatives.** The Etsy and jewelry communities are almost all early-stage hobby sellers. Established creative owners at $100K+ don't talk there, and the interior-designer communities weren't reached.
- **Channels.** There is no measured evidence on which channel converts. The channel findings are inferences.
- **Sizing.** Unavailable. Autocomplete shows related searches exist but gives no volume.

The run stopped once the depth bar was met and a search of all 2,473 documents for the "busy / more work" objection turned up only themes already banked.

---

## 2. The desire map

Scores are 1-9 judgements against the evidence (scope / urgency / staying power). There is no demand proxy for any desire because no volume tool was reachable.

### D2. "Stuck at the same number for years, and I can't pin down why" — rank 1, recommended lead
- **In their words:** "I've been stuck at $200k in revenue for three years now" (R31, 103 points, 94 comments). Also "Stuck at $300K" after 26 years (R32), "stuck around the $1.5m revenue mark for the past 4 years" (R33), and "something's off, growth's stalled, margins are weird... but they can't pin down *what*" (R14).
- **Why-chain:** I want help growing [OBSERVED R11] → revenue has been flat for years despite more effort [OBSERVED R31, R37] → I can't pin down what's wrong [OBSERVED R14] → my work isn't turning into money I keep [INFERRED R36, R41] → I'm not sure what I built will ever give me the security I started it for [INFERRED R35, R32].
- **Hell:** another December looking at the same annual number. She has tried new products, more posting and another channel, and still "lose[s] a customer for every one we gain" (R31). Her calendar is fuller than ever and the month ends where it started (R37).
- **Heaven:** she knows which one change moved the number (a price, a repeat-purchase program, a sales step), can point to it in her books, and finally pays herself fairly (R19).
- **Scores:** scope 7, urgency 6, staying power 7. "Stuck" appears in 64 of the 2,473 documents.
- **Intensity:** keep-me-up-at-night [INFERRED: years of frustration, money set aside to spend].
- **Can Founder Forum serve it honestly?** Yes. Month 1 diagnoses from her goals, numbers and operations, and the market's own experts say the stated problem is often not the real one (R23). It cannot promise the result.
- **Instinct / problem:** Control (certainty) / Complexity.

### D1. "Someone who's actually done it, to sanity-check my decisions" — rank 2, used as the proof inside D2
- **In their words:** "I don't have a clear, actionable plan to get there, and I don't have anyone experienced enough around me to sanity-check my decisions" (R11). "I would only ever consider someone who's actually operated at a successful level" (R25). "Coaching isn't useless. Paying people money who have no experience doing the thing they are coaching in is useless" (R02, 102 points).
- **Why-chain:** I want an advisor who has run a business [OBSERVED R25, R02] → advice from people who hadn't done it was useless [OBSERVED R01, R20] → I need my decisions checked [OBSERVED R11] → alone I second-guess myself [OBSERVED R21] → I want to make big calls with confidence [INFERRED R21, R24].
- **Hell:** "$800/month... A google doc with a 90 day plan I couldve made myself and 3 zoom calls where she mostly asked me questions and took notes" (R01, 323 points).
- **Scores:** scope 6, urgency 6, staying power 6. Intensity: keep-me-up-at-night [INFERRED].
- **Fit:** strong on proof. Sallie's record as stated in the ground truth (CEO-for-hire at six companies, law-firm CEO, led a ~300-rep sales team) clears the "has actually done it" bar. The risk is buyers who want same-industry experience (R02).

### D4. "Profit and a fair paycheck, not just revenue" — rank 3
- "I have a business coach and he has helped me turn my business from doing a liitle over break even to now running a 17.5% net profit while taking a fair paycheck of over 75k" (R19). "I haven't gotten a paid more than I need to survive at any point in the last 20 years" (R36). Owners describe a "hire help → lose profit → take it back on yourself" cycle (R41).
- Scores: scope 5, urgency 5, staying power 7. Intensity: annoyance [INFERRED]. Fit: good (pricing and owner pay are named levers). Confidence: low.

### D3. "Get out of the weeds / stop being the bottleneck" — rank 4
- "I'm still the bottleneck for hiring, sales, and a bunch of day-to-day stuff" (R11). "running on a treadmill at full speed but staying in the exact same spot" (R37). "One day, when the business runs itself, it'll be all worth it" (R43).
- Scores: scope 6, urgency 6, staying power 8. Intensity: keep-me-up-at-night.
- **Fit is only partial, which is why this isn't the lead.** Founder Forum builds process in months 4-6 but does no done-for-you work. "Off my plate" in this market partly means someone doing the work (R47). Leading with workload relief would promise what months 1-3 don't deliver.

### D5. "Not doing it alone" — rank 5, a supporting benefit
- "It's lonely as a small business owner in the sense where I have no one to share my struggles with" (R21). Women founders ask for "a small 'squad' of 10-12" instead of "huge, noisy 2,000-person communities" (R27). That matches the 8-10 group size. Intensity: must-be-nice.

### Lead, policy and plateau plan
- **Lead with D2, using D1 as the mechanism and proof and D4 as the payoff.** "You've been stuck at the same number, and it isn't for lack of effort. Someone who has run companies reads your actual numbers and finds the one move."
- **Weighting policy:** this is pre-launch, with 7 members needed by Oct 14, ads capped and no cold outreach. So urgency, reachability and fit outrank raw scope. D3 has similar scope but fails the "can we honestly deliver it" gate as a lead.
- **Plateau plan:** first vary the hooks on D2, then move to D4, then D3 framed honestly around months 4-6.
- **A person should confirm this lead before spending against it.** The packet holds only part of the product knowledge the delivery gate depends on.

### The relief question: does help read as "more work"?
- **The exact objection isn't in the public corpus** [OBSERVED, low]. "One more thing" appears 0 times, "less busy" 0 and "on my plate" 0 across 2,473 documents. It rests on what Sallie hears on calls. Missing from a sample doesn't mean missing from the market.
- **What owners fear is paying for nothing** [OBSERVED, high]: "mostly vibes" (R01), "you're paying for someone's time, not their results" (R07), "basically a glorified personal journaller" (R08), and a Tony Robbins-certified coach whose fees "would have been much more beneficial" in an index fund (R20).
- **So "more work" is probably the polite surface of "more work with no payoff"** [INFERRED, medium]. In these threads, help feels like relief when it:
  1. starts from her real books and names one move (R13, R23)
  2. is hands-on, not generic (R03)
  3. ties the fee to a measurable result (R06, R07)
  4. has an end point (R17)

  **Founder Forum already does all four:** month-1 diagnosis from her numbers, support between calls, a success fee measured from her books, and a six-month term with exit any time. The relief message is in the terms, not in a promise of less work.
- **Test it** [ASSUMPTION]: log the busy-season objection word for word on every call until Oct 14 (TM5).

---

## 3. Phrase bank (verbatim)

**How they name the problem:** "stuck at $200k in revenue for three years" (R31) · "I keep circling the same problem" (R11) · "running on a treadmill at full speed but staying in the exact same spot" (R37) · "Busy wasn't the same as growing" (R38) · "something's off, growth's stalled, margins are weird" (R14) · "I'm still the bottleneck" (R11) · "I sometimes get stuck in the weeds" (R18) · "break through the revenue ceiling" (R32) · "scaling when hitting a time/ cash flow ceiling" (R28) · "I can't trust someone else to do my work" (R40) · "It's lonely as a small business owner" (R21) · "there's a “missing piece” I'm not seeing" (R39)

**How they describe the failed alternative:** "A google doc with a 90 day plan I couldve made myself" (R01) · "is it mostly vibes?" (R01) · "more like televangelists than actual operators" (R11) · "“unlock your potential” energy" (R11) · "a glorified personal journaller" (R08) · "you're paying for someone's time, not their results" (R07) · "approaching it like I was a creative who knew nothing about business" (R22) · "can't justify a $500+/mo retainer for something I can't tell is working" (R44)

**How they describe success:** "a 17.5% net profit while taking a fair paycheck of over 75k" (R19) · "I can track a significant increase in my revenue" (R02) · "maintain the 10,000 foot view" (R18) · "when the business runs itself" (R43) · "take a big chunk of it off my plate" (R47)

**Category words:** business coach, consultant, **mentor** (54 documents), advisor, **operator** (16), mastermind, accountability (38), fractional CFO, SCORE mentor.

**Not found in this corpus** (2,473 documents from 36 Reddit threads, Jan 2025 to Oct 2026): "one more thing", "less busy", "relief", "boss babe", "girlboss". Barely present: "growth plan" (1), "maxed out" (1), "not ready" (1). That means these words carry no evidence of buyer usage here, not that buyers never say them. "Growth plan" is still an accurate description of what Founder Forum delivers, so it may stay as a product term. It just isn't the hook.

---

## 4. Avatar

### A1: the owner stuck at the same number [stage: considering] [evidence: hypothesis]
Core: owners of established, customer-backed businesses stuck at about the same revenue for a year or more who can't pin down why (D2).

1. **Persona:** This is for a woman running an established business with customers that has been stuck at about the same revenue for a year or more, who has already tried more marketing, new products, DIY research and perhaps a coach, and who needs to see that the person helping has actually run and grown companies, and that the fee is tied to results, before buying.
2. **Trigger:** another year at the same number (R31, R33), or about to make a big bet such as wholesale, PR or an agency (R24, R32, OB1).
3. **Failed alternatives:** more marketing, SEO and new products (R31, R33); ChatGPT or Claude; free SCORE mentors (R16); coaches with no operating record (R01, R20); consultants who didn't understand the business (R22).
4. **Awareness:** problem-aware ("stuck"), and solution-aware of coaching but distrustful (R01, R10).
5. **Proof path:** operator track record (R02, R25, R34); specific, measurable outcomes (R06); referrals from people she trusts (R48); a low-commitment start (R05: "I signed up for a month of service to try it out").
6. **Angle:** The argument is that being stuck at the same number for years is rarely an effort problem, it is one unidentified lever in her own numbers, so this owner can find and pull the move that matters without paying for another round of generic advice or doing more of everything.
7. **Offer frame:** The offer frames Founder Forum as paying for results, not time (a monthly fee with exit any time, plus a success fee only if she hits the goal measured from her books), because the first group starts Oct 14 and the fall is when her numbers move [ASSUMPTION: the fall urgency is the owner's view].
8. **Hook promise:** The opening promises recognition of her exact situation ("same revenue three years running, more effort every year") through plain founder-voice copy, without promising growth or naming the program first.
9. **Format:** founder-voice text or short talking-head video [ASSUMPTION].
10. **Funnel stage:** considering (warm network, referrals) first; cold second.
11. **Market and language:** US English, plain and direct, using the phrase bank. No hype.
12. **Limiting → enabling belief:** "coaches are people who couldn't make it running an actual business" (R01), and per the owner, "growth means working harder" (GT1) → "someone who has run companies will read my actual numbers and show me the one move."
13. **Identity:** before: "very good at creating... not the best at business things" (R18). After: an owner who knows her numbers.
14. **Pain ladder / desire hierarchy:** flat revenue → working harder for less, paying everyone but herself (R36, R41) → what she built feels like "something I'm chained to" (R35). Desires: break through the number → profit and a fair paycheck (R19) → a business that runs without her in every decision (R43).
14b. **Why-chain:** see D2 (each link labelled).
15. **Emotion at trigger / cost of inaction:** frustrated, exhausted, alone (R31, R37, R21). Cost: another flat year and burnout.
16. **Objections:** see section 5.
17. **Value sensitivity (hypothesis):** she will pay $800+/month but resents generic output (R01). A retainer she can't measure is a non-starter (R44). She compares against free options (R16) and prefers help with an end (R17). The success fee and exit terms are likely enabling.
18. **Evidence:** hypothesis. Built from 36 public discussions and one prospect call; no customer validation.

**Sub-avatars (angles on the same decision):**
- **A1-S1, weighing a big move** (R24, R32, OB1): "Before you spend on wholesale, PR or an agency, find out which move your numbers actually support." This fits the jewelry prospect.
- **A1-S2, the exhausted bottleneck** (R11, R37, R40): "Busy isn't growing." Be honest that "runs without me" is months 4-6.

**Excluded:** early-stage Etsy and jewelry sellers, who dominate those communities (R49, R50). They are below the fit line.

**The four sentences** are the persona, angle, offer and hook above. All four can be written from the evidence; the offer's time pressure is the one assumed part.

---

## 5. Objections

| Surface objection | The real one underneath | What answers it |
|---|---|---|
| "Business coaches are a scam" (R01, R12, R20) | "I'll pay for vibes and still have to figure it out myself" | Proof and mechanism: show what month 1 produces and who builds it. Skip "accountability / mindset / clarity" language, which lands "in the same pile as generic linkedin gurus" (R26). |
| "They haven't run a business like mine" (R02, R25) | "They won't understand my business" (R22) | Mechanism: start from her books and goals. FAQ on why owners from other industries help (R23, R30). |
| "I can't tell if it's working" (R44, R14) | No visible return | Risk reversal: success fee only on the goal measured from her books; exit any time. No ROI guarantee. |
| "I can get this free" (SCORE, AI) (R16, R15) | Free advice doesn't make me act | Mechanism: between-call support; plan, track and adjust. |
| "I can't add one more thing / wait until I'm less busy" [ASSUMPTION, owner-reported only] | More work with no payoff | Offer structure: two one-hour calls a month; month 1 is diagnosis. Test frequency (TM5). |
| "Let me talk to my husband" (OB1) [INFERRED] | The spouse is an investor who wants a low-risk case (R45) | Proof object: a one-page spouse summary of terms, exit, success fee and month-1 output (TM3). |
| "I'm a creative, not a business person" (R18) | "Don't talk down to me" (R22) | Copy guidance: talk to her as the owner who built it. |

---

## 6. Alternatives and competitor perception

- **Doing more of the same** (SEO, sales training, new products, more posting) is the real incumbent (R31, R33, R44).
- **Free mentors (SCORE / SBDC)** are the most-recommended substitute in these threads (R16, R47).
- **AI as a free strategist** comes up in most help threads, along with the reply that it "can't... keep you accountable" (R15).
- **Fractional CFOs, consultants and accountants** offer numbers-first strategy (R04, R13). This is closest to Founder Forum's month-1 diagnosis.
- **Self-organised peer groups** (R27, R30).
- **Big coaching brands** are known for big promises, high-pressure sales and an absent founder (T02, T04, R20).
- **What the market has been trained to expect:** generic advice, a plan with no follow-through, and fees for time. Every ad is arguing against that whether it says so or not.

---

## 7. Gaps in the market

| Type | Gap |
|---|---|
| Trust | The category is distrusted (R01, R10). Answer with proof objects (operator record, books-measured success fee), not features. |
| Positioning | Most coaching sells "accountability, mindset, clarity" (R26). "Pay for results, not time" and "find the one move in your numbers" are unclaimed [INFERRED]. |
| Education | Owners assume the fix is more marketing when it may be pricing, retention or capacity (R23, R33, R42). |
| Distribution | Established creative owners aren't visible in creative communities (R49), and Reddit punishes coaches who promote themselves (R10). Warm and referral channels look like the reachable path [INFERRED]. |
| Product | Some buyers want work taken off their plate (R47). Founder Forum offers referrals, not doing the work, so don't imply otherwise. |

**On channels (the decision asked):** the evidence can't rank channels by conversion. What it does show: trust in this category travels by referral ("Five years of networking and multiple referrals says a lot more than a random recommendation", R48), Reddit is hostile ground for coaches, and the creative communities hold the wrong stage of buyer. That is consistent with prioritising past clients, referrals and warm one-to-one conversations, which the owner reports as about 60% of sales today, and keeping Meta to a capped hook test [INFERRED, low].

---

## 8. Test matrix (ranked by what each would teach)

| # | Desire / intensity | One variable | Cell | Proves it wrong |
|---|---|---|---|---|
| TM1 | D2 / keep-me-up | Angle | Warm list and past clients: "stuck at the same number" vs "pay for results, not time". Same offer, split the list, send by Oct 7. | Neither gets a discovery call within 5 business days, or there is no difference |
| TM2 | D2 / keep-me-up | Channel | A specific referral ask to past clients ("who do you know who's been stuck at the same revenue?") vs Meta at current spend, 10 days | Referral asks get 0 calls while Meta gets at least 1 |
| TM3 | D1 / keep-me-up | Proof | Spouse one-pager for "talk to my husband" prospects vs none | No faster decisions within 7 days |
| TM4 | D2 / keep-me-up | Hook | Meta inside the cap: "same revenue three years running?" vs the current creative, equal spend for 2 weeks | No difference in booked-call rate |
| TM5 | (measurement) | Objection log | Log every objection word for word on calls until Oct 14 | Busy-season objection appears on under a third of calls |

---

## 9. Gaps and asks (cheapest first)

1. **Who actually buys** [ASSUMPTION]: pull the last 10 discovery calls and past clients, and count industry, revenue band and whether the plateau trigger applies. The public corpus can't settle "women creatives at $100K+".
2. **Why past clients said yes** [ASSUMPTION]: 15 minutes each with Sarah K. and Fraulein Boots, recorded word for word. This is the cheapest high-value evidence available.
3. **Busy-season objection frequency** [ASSUMPTION]: TM5.
4. **Usable proof** [ASSUMPTION]: records and permissions for the $280K and $56K → $1M results and the testimonials. Until then they can't be stated as fact.
5. **Demand size** [ASSUMPTION]: Google Keyword Planner or Trends from a normal browser for "business coach for women entrepreneurs", "how to scale a small business" and "small business growth plan". Record provider, geography, window and exclusions.
6. **Interior designers** [ASSUMPTION]: their business conversation wasn't reached. Search Houzz Pro or designer Facebook groups by hand, or ask two past designer clients what they read.

**Claims gate flags:** no income or results guarantees (the plateau angle promises diagnosis, not growth). Client results stay out of copy until records and permissions exist. R18 and R19 are anonymous Reddit voices, never testimonials. Prospect L.W.'s words are not for marketing. 10x ROI only as a target.

This packet writes no ads, pages or emails, and it doesn't decide spend.
