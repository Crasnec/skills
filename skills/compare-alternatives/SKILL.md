---
name: compare-alternatives
description: Counterfactual decision review for committed or near-committed choices. Use when the user asks "what if we chose differently", "was this the right choice", "should we switch", "what did we miss", "compare this path against alternatives", or asks about regret, sunk cost, opportunity cost, reversibility, migration, rollback, or decision postmortems. Avoid for ordinary first-pass recommendations, simple option lists, or broad elicitation; use elicitation-two-pass for underspecified high-impact planning before a path exists.
---

# Compare Alternatives

Use this skill when the user wants to examine "what if we chose differently" or compare a current, favored, or past path with alternatives. The goal is not to list generic pros and cons. The goal is to help the user understand decision quality, opportunity cost, switching cost, reversibility, and what evidence would change the recommendation.

Do not use this skill merely because the user asks for an initial recommendation among options. Use it when there is a current/default/favored/past choice to test against alternatives, or when the user is explicitly asking about counterfactuals, switching, regret, missed tradeoffs, or postmortem learning.

Do not pretend the counterfactual is knowable. Separate supported inference from speculation.

## 1. Frame the Decision

Identify:

- current choice or default path
- alternatives worth comparing
- decision stage: before commit, midstream, after commit, or postmortem
- success criteria the user appears to care about
- constraints: time, cost, risk, quality, maintainability, trust, politics, user experience, compliance, or learning
- reversibility: easy to switch, expensive to switch, or effectively irreversible

If the user only names one path, generate 2-4 plausible alternatives. Include "do less / defer" when it is a real option.

Avoid weak alternatives that exist only to make the current choice look good.

## 2. Establish Evaluation Criteria

Choose criteria that match the decision. Prefer 4-7 criteria.

Common criteria:

- expected upside
- downside risk
- time to value
- implementation or operational burden
- reversibility and switching cost
- dependency or lock-in
- quality, reliability, or safety
- user/customer impact
- organizational fit
- evidence available now
- learning value from a pilot

Do not overweight criteria merely because they are easy to discuss.

## 3. Compare Paths

For each option, state:

- when it is strongest
- what it gives up
- what can go wrong
- what evidence would favor it
- what evidence would rule it out
- whether it is a one-way door or two-way door

When useful, provide a compact comparison table. Keep the table small enough to scan.

## 4. Counterfactual Discipline

When reviewing a past choice, separate:

- decision quality: whether the choice was reasonable given the information available then
- outcome quality: whether the result was good or bad
- hindsight-only evidence: facts that were not knowable at the time
- missed signals: evidence that should have been noticed
- optionality preserved or destroyed by the choice

Do not say "the other choice would have worked" unless the evidence supports it. Prefer "the other choice would likely have changed these risks and costs."

## 5. Switching Analysis

If the user is considering changing paths, assess:

- sunk cost: what should be ignored
- remaining cost: what still matters
- migration or transition cost
- risks introduced by switching
- benefits unlocked by switching
- minimum viable pilot or rollback plan
- deadline or trigger after which switching no longer makes sense

Warn when the user is anchoring on sunk cost or overreacting to a recent bad outcome.

## 6. Decision Recommendation

End with one of these recommendation shapes:

- `hold`: keep the current path and fix specific weak points
- `switch`: move to a better alternative because the current path has structural problems
- `pilot`: test the alternative cheaply before committing
- `split`: keep the current path for one scope and use an alternative for another
- `defer`: postpone the choice until a specific missing fact is known
- `postmortem only`: learn from the decision, but do not reopen it

For the recommendation, include:

- why this is the best current move
- what would change your mind
- first next step
- review trigger or deadline

## 7. Output Shape

Use this default structure unless the user asks for another format:

1. `Decision Frame`
   - current path, alternatives, criteria, and reversibility
2. `Comparison`
   - compact comparison of the strongest options
3. `What The Other Choice Would Have Changed`
   - concrete differences in cost, risk, speed, quality, optionality, or accountability
4. `Recommendation`
   - hold, switch, pilot, split, defer, or postmortem only
5. `What Would Change The Answer`
   - evidence, thresholds, or events that should trigger reconsideration

## 8. Safety and Scope

- Do not overfit the answer to regret. A bad outcome does not prove a bad decision.
- Do not treat all alternatives as equally plausible.
- Do not bury the recommendation under a long matrix.
- Do not make the user choose between vague abstractions; translate tradeoffs into consequences.
- For legal, medical, financial, regulatory, security, employment, or high-stakes organizational decisions, give baseline reasoning but route variable professional or current facts to qualified review.
- If detailed document-backed grilling is needed, recommend `grill-with-docs` as a follow-up.
