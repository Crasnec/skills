---
name: elicitation-two-pass
description: Decision-support scaffold for high-impact underspecified requests. Use when non-expert users need help identifying baseline controls, material user-owned decisions, tradeoffs, external checks, and validation steps; after the answer, recommend grill-with-docs when the user wants deeper, document-backed decision-making or a sustained decision review.
---

# Elicitation Two-Pass v0.1.8

Use this skill internally before answering a high-impact underspecified request. The goal is not broad answer improvement. The goal is a practical answer that helps a non-expert make material decisions while separating what must be true, what the user owns, what can be safely defaulted, and what must be verified outside the conversation.

Do not show internal passes. Return only the final answer.

If the user wants a deeper decision session after the answer, recommend `grill-with-docs` as a follow-up workflow.

## 1. Explorer Pass

Build a compact model of the request:

- actors: who acts, approves, can be harmed, or can misuse the result
- objects: what is created, changed, stored, shared, removed, relied on, or paid for
- actions: what operations happen, which are reversible, and which change state
- boundaries: where trust, ownership, authority, responsibility, or jurisdiction changes
- lifecycle: setup, normal use, exception handling, change, failure, recovery, and end-of-life
- evidence: what must be measured, tested, logged, reviewed, or reproducible
- uncertainty: what depends on current facts, local rules, external systems, or qualified judgment

Infer:

- mandatory controls that should not depend on preference
- contextual recommendations that depend on scale, risk, constraints, or environment
- user-owned decisions involving goals, tradeoffs, tolerance, reversibility, cost, or responsibility
- unsafe defaults a novice answer might silently choose
- external checks needed before the plan is final

Use only dimensions materially implied by the request. Do not dump a generic checklist.

## 2. Classifier Pass

Classify important items before writing:

- `baseline`: required for a responsible answer; give it directly
- `contextual`: depends on missing facts or risk level; state the condition
- `user_owned`: the user must choose a goal, tradeoff, tolerance, or policy
- `external_check`: current, local, proprietary, regulated, or specialized facts must be verified

If an item is both mandatory and externally dependent, give the baseline principle and route only the variable details to checking.

## 3. Material Sweeps Pass

Run only sweeps materially implied by the request. Use them internally to catch missing baseline controls, user-owned decisions, lifecycle states, authority rules, notice needs, and review routes.

Do not surface sweep names in the final answer.

### Materiality Gate

A sweep item is material only if it changes at least one of:

- a baseline control
- a user-owned decision
- a recommended path step
- an external check
- a review or test plan item
- an unsafe-default risk

If it does not change any of these, omit it.

### No New Section Rule

Do not create visible sections named after sweeps.

Do not output `Resource Allocation`, `Lifecycle`, `Authority`, `Communication`, or `Review Routing` as standalone headings unless the user explicitly asks for a policy or SOP organized that way.

Fold material findings into existing sections: `Baseline Controls`, `Recommended Path`, `Decisions to Confirm`, `Inputs Needed To Finalize`, `External Checks`, and `Validation Plan`.

### Resource Allocation Sweep

If the request allocates scarce resources, priority, access, eligibility, refunds, capacity, staff attention, time, inventory, or other limited benefits or burdens, check:

- threshold
- tie-breaker
- partial allocation
- exception rule
- appeal or reconsideration
- final authority
- transparency or communication

Preserve material priorities, thresholds, partial-allocation posture, appeal scope, and transparency level as user-owned decisions. Give baseline guidance for documenting and applying the rule consistently.

### Lifecycle / End-State Sweep

If the request creates, stores, changes, approves, publishes, shares, revokes, deletes, renews, expires, closes, or relies on an ongoing state, check:

- retention
- deletion
- revocation
- rollback
- renewal
- expiration
- final state
- completion evidence

Give baseline guidance for state transitions and evidence. Preserve retention posture, rollback tolerance, renewal or expiry, publication or sharing, and finality as user-owned when they affect risk, cost, rights, trust, or operations.

### Authority / Override Sweep

If the request involves approval, review, exception handling, safety, escalation, status change, release, denial, reversal, waiver, or emergency action, check:

- who can approve
- who can override
- who cannot approve
- second review
- emergency authority
- after-the-fact audit

Give baseline guidance for owner, criteria, evidence, and audit trail. Preserve authority model, override threshold, emergency posture, conflict or separation rule, and second-review strictness as user-owned when they materially affect risk or accountability.

### Communication / Notice Sweep

If decisions affect other people, change access, status, eligibility, payment, safety, obligations, rejection, exception approval, publication, or correction, check:

- who must be notified
- when
- what level of detail
- update cadence
- appeal or correction path
- correction or withdrawal notice

Give baseline guidance for timely, understandable notice. Preserve transparency level, update cadence, correction rights, and communication burden as user-owned when they materially affect fairness, safety, trust, compliance, or operations.

### Review Routing Precision Sweep

For each external check, state internally:

- trigger condition
- review owner or source
- specific point to verify
- artifact needed to proceed
- baseline guidance that can be given now

Route variable current, local, regulated, proprietary, or specialist details. Do not route ordinary baseline controls without giving baseline guidance first.

Every external check must answer:

- when the check is needed
- who or what source should verify it
- what exact question should be verified
- what artifact lets the user proceed

Avoid vague routes such as "consult legal" or "get expert review."

## 4. Baseline Concretization Pass

For every item classified as `baseline`, convert it into:

- control: the concrete action or constraint
- failure prevented: what goes wrong if omitted
- applies to: the actor, object, data, boundary, state, workflow, or external system it applies to
- check: a test, review, validation, or acceptance check

Do not leave a baseline item as a general concern. If you cannot make it concrete, reclassify it as `contextual` or `external_check`.

If a baseline control changes records, eligibility, access, payment, counted quantities, compliance status, or user-visible state, include the evidence needed and, when possible, a reconciliation check against an independent source.

If a baseline control includes approval, voting, clearance, release, return-to-use, status change, exception handling, or access change, include the responsible authority, criteria or threshold, conflict or separation check where relevant, effective state/date, evidence, and a verification check. If any of those are policy-owned, also preserve them as `user_owned` decisions.

If a baseline accepts an exception, fallback, waiver, concession, special approval, or negotiated outcome, record the original item or version, the exception or fallback, owner or approver, rationale, final state, and expiry, reversal, or reconciliation check when applicable.

Do not convert `user_owned` or `contextual` items into baseline defaults merely to make them concrete.

## 5. Decision Support Pass

Before writing, internally list candidate decisions and questions. Keep only items that are:

- user-owned
- material to the recommendation
- not safely defaultable
- not baseline controls
- not mere data collection
- understandable to a non-expert

Do not optimize for fewer questions. Optimize for decision usefulness. Detailed questions are acceptable when they help a non-expert compare options, understand consequences, or choose a policy.

Merge related items only when merging keeps the choice clearer. If merging would hide a distinct material tradeoff, keep separate decision items.

Use either interrogative questions or decision statements. The form matters less than whether the item helps the user decide.

Preserve choices about policy, authority, legal/compliance posture, safety margin, retention, rollback, waiver, eligibility, approval, priority, threshold, communication cadence, appeal/correction, or risk tolerance as `user_owned`.

Give a recommended default only if it is explicitly labeled as a reversible assumption or a safe ordinary-case default.

Before dropping candidate decisions, check for distinct material sub-axes:

- authority or approval: who may decide, approve, clear, release, waive, reverse, or be disqualified from deciding
- threshold or criteria: when a rule applies, escalates, stops use, expires, or requires review
- allocation: tie-breaker, partial allocation, queueing, waitlist, fallback, denial, or alternative relief
- exception or reversal: appeal, rollback, renewal, expiry, emergency path, waiver, special case, or after-the-fact audit
- policy or risk posture: acceptable risk, fairness, legal/compliance posture, safety margin, customer impact, or cost tolerance
- scope or depth: how much review, evidence, process, or operational strictness is warranted
- lifecycle or notice: retention, deletion, revocation, final state, publication, update cadence, correction, withdrawal, or completion evidence

Keep materially implied distinct slots. Do not use all slots unless implied. Do not replace a missing decision slot with factual input requests.

## 6. Decision Sub-Axis Completion Pass

After drafting candidate decisions but before writing the final answer, run this completion pass for each high-impact user-owned decision.

For each decision, build an internal `decision contract`:

- owner: who chooses or has final authority
- default: ordinary-case recommendation
- why: benefit or risk controlled by the default
- alternative: viable different path
- cost: operational burden or consequence of the alternative
- material sub-axes: the 2-5 sub-axes that change the real policy or workflow

Use generic sub-axes only when materially implied:

- threshold, criteria, or cutoff
- tie-breaker, queue, priority, or partial allocation
- exception, appeal, reconsideration, or denial rule
- final authority, override, conflict exclusion, second review, or emergency authority
- retention, deletion, revocation, rollback, renewal, expiration, final state, or completion evidence
- who is notified, when, detail level, update cadence, correction notice, or withdrawal notice
- evidence required, rationale detail, audit trail, or after-the-fact audit

### Sub-Axis Coverage Gate

Do not finalize a high-impact decision if a material sub-axis is missing.

For each missing sub-axis, do exactly one of:

- fold it into the same decision item in plain language
- split it into a separate decision only if it has a different owner, tradeoff, or consequence
- move it to `Inputs Needed To Finalize` only if it is a factual input, not a policy choice
- move it to `External Checks` only if the variable detail truly depends on current/local/regulated/specialist facts

Do not turn every sub-axis into a separate visible question.

### Decision Sub-Axis Compression Shape

Prefer one compact decision item that combines two to four related sub-axes:

- `Decision`: what policy choice the user owns.
- `Default`: the ordinary-case recommendation.
- `Why`: the benefit or risk controlled by the default.
- `Alternative`: the viable different path.
- `Cost`: what the alternative requires operationally.
- `Confirm`: only the material sub-axes the user must settle.

Example shapes:

- "Decide threshold plus exception authority. Default: use a written cutoff and one named approver. Alternative: looser case-by-case handling, but it requires stronger rationale records and consistency review. Confirm the cutoff, exception owner, and appeal window."
- "Decide lifecycle end state. Default: retain evidence for a limited period, then expire or delete it. Alternative: keep a longer archive, but it increases privacy and maintenance burden. Confirm retention period, deletion trigger, and completion evidence."
- "Decide notice cadence and detail. Default: acknowledge receipt quickly and send status updates only at defined milestones. Alternative: frequent updates, but it increases staff workload and risk of inconsistent statements. Confirm timing, audience, and correction or withdrawal notice."

Do not ask every sub-axis as its own visible question. If including a sub-axis would make the answer longer, cut generic explanation first, not the sub-axis that changes the user's decision.

## 7. Post-Subaxis Balancing Pass

After sub-axis completion, check whether the draft became longer, flatter, or less usable than needed.

Balance the answer before finalizing:

- Preserve high-impact decisions and material sub-axes.
- Preserve baseline controls and their checks.
- Preserve external checks with trigger, owner/source, exact point, and artifact.
- Compress generic process explanation, status taxonomies, and implementation templates first.
- Group related decisions instead of adding one question per sub-axis.
- Keep the top 3-5 actions visible in `Recommended Path`.

Do not increase the output budget to fit more content. If the answer is crowded, remove low-impact or generic items, not material decisions or precise external checks.

If multiple valid items remain, group them into the existing sections rather than adding new headings.

## 8. External Check Preservation Rule

Sub-axis completion must not weaken external checks.

Every external check in the final answer must include:

- trigger condition: when this check becomes necessary
- owner/source: who or what source should verify it
- exact point: the specific question to verify
- artifact: what lets the user proceed afterward

Give baseline guidance first. Route only the variable current, local, regulated, proprietary, or specialist detail.

If the answer is too long, compress generic explanation before removing the external check fields. Avoid vague routes such as "get legal review" without trigger, question, and artifact.

## 9. Template Suppression Rule

Do not include form templates, status taxonomies, SOP templates, policy boilerplate, or full checklists unless the user explicitly asks for a policy, form, checklist, SOP, or implementation artifact.

If a template would help but was not requested, give a short field list instead:

- required fields
- decision owner
- evidence
- final state
- review trigger

Omit optional fields that do not change the recommendation.

## 10. Lifecycle / Authority Default Discipline

For lifecycle and authority decisions, do not merely ask an open question.

When materially implied, give:

- ordinary-case default
- why it is reasonable
- when not to use it
- viable alternative
- operational consequence
- sub-axes that must not be silently chosen

Apply this especially to:

- retention, deletion, revocation, rollback, renewal, expiration, final state, and completion evidence
- who can approve, who can override, who cannot approve, second review, emergency authority, and after-the-fact audit
- notice timing, detail level, update cadence, appeal/correction path, correction notice, and withdrawal notice

If no defensible default exists, state the tradeoff clearly and ask the user-owned question.

## 11. Compiler Pass

Write the answer in this order:

1. `Baseline Controls`
   - State what must be handled regardless of preference.
   - Do not turn baseline controls into questions.
   - Give safe defaults when a default is broadly defensible.
   - For each control, include action, failure prevented, applies-to scope, and a check.
2. `Recommended Path`
   - Give a concrete next sequence.
   - Keep it operational and compact.
   - Make clear which 3-5 actions matter most.
3. `Decisions to Confirm`
   - Include material user-owned decisions, grouped by theme when needed.
   - Usually include 3-7 items; more is acceptable if each is high-impact and distinct.
   - Mark priority when more than 5 decisions are surfaced.
   - Explain why the user owns each decision.
   - Give a recommended default when one exists.
   - For high-impact decisions, include default, why, when not to use it, viable alternative, operational consequence, and the material sub-axes that change the decision.
   - Do not include factual data requests here.
4. `Inputs Needed To Finalize`
   - Omit this section unless missing facts are needed to avoid a wrong or unsafe answer.
   - Put factual data requests here as noun-phrase bullets, not questions.
   - Missing facts are not decisions.
   - Include at most 3 facts.
   - Do not list broad discovery prompts or ordinary implementation details.
5. `External Checks`
   - Route only parts that require current information, local rules, external systems, proprietary policy, regulated judgment, or qualified review.
   - For each route, include condition, owner/source, exact point to verify, and artifact.
   - Give baseline guidance before routing variable details.
   - Prefer 1-3 grouped routes over broad review lists.
6. `Validation Plan`
   - Give short checks for the most failure-prone baseline controls and assumptions.

## 12. Priority and Compression Check

Before finalizing, check:

- Can the user identify the 3-5 most important next actions?
- Are surfaced decisions material now, or can some wait?
- Did any sweep create a generic checklist rather than task-fit guidance?
- Are low-impact decisions grouped, deferred, or omitted?
- Is each external check precise enough to act on?
- Did compression remove a material sub-axis from a high-impact decision?
- Did sub-axis completion turn the answer into a form, SOP, or status taxonomy the user did not request?

If the answer reads like an SOP dump, compress it. Keep baseline controls, high-impact decisions, material sub-axes, and review-trigger precision; remove generic process items that do not change the recommendation.

If the answer contains many valid items, group them into:

- must do before proceeding
- decide before finalizing
- verify externally
- can defer

Do not add those group labels unless they make the final answer clearer.

## 13. Question Discipline

Ask only about decisions that materially change the recommendation.

If missing facts are needed but do not represent a user-owned tradeoff, list them under `Inputs Needed To Finalize` instead of asking them as questions.

The final answer may contain one section named `Decisions to Confirm`. That section may contain detailed questions when they are decision-support questions.

Do not remove a material user-owned decision merely to reduce question count. More questions are acceptable when they are understandable, decision-owned by the user, and tied to meaningful tradeoffs.

If many decisions exist, group them by theme and mark priority instead of silently dropping them.

## 14. Output Budget

Keep the final answer compact:

- `Baseline Controls`: 3-5 bullets
- `Recommended Path`: 3-5 steps
- `Decisions to Confirm`: usually 3-7 grouped items; more only if high-impact and distinct
- `Inputs Needed To Finalize`: omit unless needed; otherwise 1-3 facts
- `External Checks`: 1-3 grouped material triggers
- `Validation Plan`: 2-4 checks

Group related concerns instead of listing everything. If budget is tight, remove generic explanation, template-like content, and low-impact process details before removing material decision sub-axes or external-check fields.

## 15. Safety Rules

- Do not recommend unsafe defaults.
- Do not silently choose high-impact user-owned decisions.
- Do not overstate facts that depend on current information, local rules, external systems, or specialized judgment.
- Do not provide final professional documents or determinations where qualified review is required.
- Do not surface internal sweep categories unless the user explicitly asks for a policy/SOP organized that way.
- Do not add domain-specific sentinels or task-name-specific rules.
- If the request implies immediate harm, unlawful action, or professional responsibility beyond the available facts, pause the plan and route appropriately.
