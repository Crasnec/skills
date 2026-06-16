---
name: course-correct
description: Work checkpoint and course-correction scaffold for nontrivial ongoing tasks. Use when the user asks to assess direction, compare before/after, decide whether to continue, adjust, backtrack/BACK, rollback, pause, or when a long-running implementation, cleanup, migration, refactor, research loop, or skill iteration reaches an intermediate result that may be wrong. Avoid for simple one-shot tasks or ordinary option comparison; use compare-alternatives for evaluating strategic choices outside an active work session.
---

# Course Correct

Use this skill to decide whether ongoing work is moving in the right direction. The goal is not to produce a long retrospective. The goal is to preserve momentum while catching wrong turns early.

Do not show internal deliberation. Give a compact checkpoint decision.

## 1. Trigger Discipline

Use this skill when:

- the user explicitly asks for direction check, before/after comparison, "계속할까요", "BACK", rollback, backtrack, or course correction
- a multi-step task has produced an intermediate artifact that changes the next step
- test results, user feedback, screenshots, diffs, or benchmark results suggest the current path may be wrong
- a cleanup, migration, refactor, or skill iteration could destroy useful work if continued blindly

Do not use it merely because work is ongoing. Simple tasks should continue normally.

## 2. Establish The Checkpoint

Identify:

- original objective
- current plan or current path
- before state: what was true before the latest change
- after state: what changed
- evidence available now: tests, diffs, screenshots, user feedback, metrics, logs, or manual inspection
- constraints: user intent, safety, reversibility, time, blast radius, and uncommitted changes

If the original objective is unclear, infer the nearest concrete objective from the conversation and state it briefly.

## 3. Compare Before And After

Evaluate the latest change against the objective:

- improved: what is clearly better
- regressed: what got worse or riskier
- unchanged: what the change failed to affect
- unknown: what still lacks evidence
- side effects: unrelated changes, new complexity, or hidden maintenance burden

Prefer concrete artifacts over impression. Use file paths, metrics, screenshots, test output, or exact behavior when available.

## 4. Direction Decision

Choose exactly one primary decision:

- `CONTINUE`: direction is right; proceed with the next planned step
- `ADJUST`: direction is mostly right, but change tactics before continuing
- `BACK`: current path is wrong enough that continuing would compound cost; revert, unwind, or return to a previous checkpoint
- `PAUSE`: do not continue until missing evidence or user-owned input is resolved

Use `BACK` only when there is a specific previous state or smaller scope to return to. Do not use it as a vague criticism.

Use `PAUSE` when the next action depends on user intent, external state, credentials, destructive approval, or high-risk unknowns.

## 5. Backtrack Discipline

If recommending `BACK`, state:

- back target: exact checkpoint, commit, file state, design point, or artifact version
- reason: the failure that makes the current path not worth salvaging
- salvage: what should be kept from the attempt
- undo method: targeted patch, revert commit, delete generated artifact, branch off, or rebuild from a smaller scope
- verification after back: how to know the backtrack succeeded

Never run destructive git commands or delete broad work without explicit user approval unless the user already clearly requested that cleanup.

## 6. Adjust Discipline

If recommending `ADJUST`, state:

- what to keep
- what to change
- what not to touch
- next test or evidence point
- failure trigger that would cause `BACK` later

Avoid "continue but be careful" as a recommendation. Convert it into a concrete adjustment.

## 7. Continue Discipline

If recommending `CONTINUE`, state:

- why the current direction is supported
- the next 1-3 actions
- the next checkpoint condition
- what would change the decision

Do not over-celebrate. Continue because evidence supports it, not because the work is incomplete.

## 8. Output Shape

Use this compact structure:

```text
Checkpoint: <one sentence>
Decision: CONTINUE | ADJUST | BACK | PAUSE

Before -> After:
- ...

Evidence:
- ...

Why:
- ...

Next:
- ...
```

For `BACK`, replace `Next` with:

```text
Back Plan:
- target:
- salvage:
- undo:
- verify:
```

## 9. Safety Rules

- Do not hide uncertainty.
- Do not keep pushing forward just because work has already been done.
- Do not recommend backtracking without a concrete target.
- Do not turn every minor issue into a checkpoint.
- Do not erase user work silently.
- Do not treat user feedback as noise; if the user says the direction feels wrong, reassess from the objective.
