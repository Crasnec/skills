---
name: work-harness
description: Execution harness for long-running, iterative, or risky agent work. Use when the user explicitly asks for a harness, recursive improvement loop, repeated experiment/evaluation cycle, checkpointed implementation, before/after assessment, or wants the agent to continue only while direction is improving and consider ADJUST/BACK/PAUSE when evidence turns negative. Avoid for simple one-shot tasks, ordinary coding changes, or strategic option comparison; use course-correct for a single checkpoint and compare-alternatives for non-active strategic choices.
---

# Work Harness

Use this skill to run nontrivial work as a controlled loop. The goal is to make progress while preserving the ability to stop, adjust, or backtrack before a wrong path compounds.

Do not turn every small action into ceremony. Use the harness only when the task is long, iterative, uncertain, destructive, or explicitly requested as a harness.

## 1. Harness Contract

At the start, establish a compact contract:

- objective: what must be true when done
- success evidence: tests, metrics, artifacts, screenshots, reports, user-visible behavior, or review results
- guardrails: what must not be broken, deleted, overfit, or silently changed
- checkpoint cadence: after each meaningful artifact, failed test, metric shift, user feedback, or irreversible step
- back target: the last known good state, commit, file set, design point, or artifact version
- stop condition: budget, repeated failure, missing user decision, unsafe operation, or no further evidence

If the task is small enough that this contract would be noise, do not use the harness.

## 2. Baseline Snapshot

Before substantial edits or experiments, capture the starting state that matters:

- current files or artifacts in scope
- current behavior, scores, test results, screenshots, or known failure
- assumptions and decision criteria
- user constraints and exclusions

Use lightweight evidence. Prefer `git status`, targeted diffs, relevant tests, and concrete outputs over broad inventory.

## 3. Work Slice

Run one meaningful slice at a time:

- choose the smallest step that can produce evidence
- avoid broad refactors unless they are the objective
- keep unrelated changes out of scope
- preserve user work
- record enough evidence to compare before and after

For coding tasks, prefer targeted edits plus focused checks. For research/evaluation tasks, prefer one controlled run or comparison before expanding.

## 4. Checkpoint Gate

After each slice, compare before and after:

- improved: what is better and evidenced
- regressed: what got worse
- unresolved: what did not move
- new risk: complexity, fragility, overfitting, hidden coupling, or user burden
- confidence: high, medium, or low based on evidence quality

Choose one decision:

- `CONTINUE`: evidence supports the direction
- `ADJUST`: direction is useful but the next tactic must change
- `BACK`: current path is wrong enough to return to a known good state
- `PAUSE`: user input, external info, credentials, approval, or safety decision is needed

When only a single checkpoint is needed, apply `course-correct` semantics and keep the response compact.

## 5. Back And Salvage Rule

If the decision is `BACK`, state:

- back target
- what failed
- what to salvage
- exact undo approach
- verification after undo

Do not use destructive git operations, broad deletion, or irreversible cleanup unless the user explicitly requested that operation or already approved the cleanup scope.

## 6. Iteration Discipline

Continue iterating only while:

- each slice has a clear purpose
- evidence is improving or the adjustment is specifically justified
- the next action still serves the original objective
- the work has not become overfit to the latest test or feedback
- the user has not given a newer conflicting instruction

Stop or pause when:

- the same failure repeats across three meaningful attempts
- progress is only cosmetic
- improvement in one metric hides regression in another
- the next step requires a user-owned decision
- the next step risks deleting or overwriting valuable work

## 7. Final Audit

Before finishing:

- verify the objective against the success evidence
- summarize important before/after changes
- report checks run and checks not run
- identify residual risk
- state whether the work should be considered done, ready for review, or still experimental

Do not call the work complete merely because a loop ended.

## 8. Output Shape

When starting a harnessed task, use:

```text
Harness:
- objective:
- success evidence:
- guardrails:
- checkpoints:
- back target:
```

At checkpoints, use:

```text
Checkpoint:
- before -> after:
- evidence:
- decision: CONTINUE | ADJUST | BACK | PAUSE
- next:
```

At finish, use:

```text
Result:
- outcome:
- evidence:
- changed:
- not verified:
- residual risk:
```

Keep these sections concise. If the user only needs progress, provide the checkpoint decision and continue.

## 9. Relationship To Other Skills

- Use `course-correct` for a single checkpoint decision inside or outside the harness.
- Use `compare-alternatives` when the user is comparing strategic paths rather than managing active execution.
- Use `elicitation-two-pass` before execution when the request is underspecified and material user-owned decisions are missing.
- Use `grill-with-docs` after the harness if the user wants deeper document-backed decision review.
