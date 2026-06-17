# skills

Codex skills maintained in this repository.

## Included Skills

### elicitation-two-pass

Decision-support scaffold for high-impact, underspecified requests. It helps Codex separate:

- baseline controls that should be handled directly
- material user-owned decisions and tradeoffs
- facts needed before finalizing
- external checks for current, local, regulated, proprietary, or specialist details
- validation steps for the riskiest assumptions

### compare-alternatives

Counterfactual decision review for comparing a current choice, plan, architecture, product direction, policy, or past decision against plausible alternatives. It helps Codex explain what another choice would have changed, whether to hold/switch/pilot/defer, and what evidence should trigger reconsideration.

### course-correct

Work checkpoint scaffold for active tasks. It helps Codex compare before/after state, judge whether the direction is improving, and decide whether to continue, adjust, BACK/backtrack, or pause before compounding a wrong turn.

### work-harness

Execution harness for long-running or iterative agent work. It wraps a task with a starting contract, before/after checkpoints, continue/adjust/BACK/pause decisions, and a final audit.

### grill-with-docs

Document-backed grilling session for stress-testing plans against a project's domain language, glossary, codebase behavior, and ADRs. It sharpens terminology and updates `CONTEXT.md` or ADRs as decisions crystallize.

## Repository Layout

```text
skills/
  elicitation-two-pass/
    SKILL.md
    agents/
      openai.yaml
  compare-alternatives/
    SKILL.md
    agents/
      openai.yaml
  course-correct/
    SKILL.md
    agents/
      openai.yaml
  work-harness/
    SKILL.md
    agents/
      openai.yaml
  grill-with-docs/
    SKILL.md
    CONTEXT-FORMAT.md
    ADR-FORMAT.md
    agents/
      openai.yaml
```

## Install From GitHub

Install one skill by pointing Codex's skill installer at the skill path:

```bash
python3 /home/adjustedmin/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo Crasnec/skills \
  --path skills/elicitation-two-pass
```

```bash
python3 /home/adjustedmin/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo Crasnec/skills \
  --path skills/compare-alternatives
```

```bash
python3 /home/adjustedmin/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo Crasnec/skills \
  --path skills/course-correct
```

```bash
python3 /home/adjustedmin/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo Crasnec/skills \
  --path skills/work-harness
```

```bash
python3 /home/adjustedmin/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo Crasnec/skills \
  --path skills/grill-with-docs
```

Install all:

```bash
python3 /home/adjustedmin/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo Crasnec/skills \
  --path skills/elicitation-two-pass \
  --path skills/compare-alternatives \
  --path skills/course-correct \
  --path skills/work-harness \
  --path skills/grill-with-docs
```

Or use a GitHub URL:

```bash
python3 /home/adjustedmin/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --url https://github.com/Crasnec/skills/tree/main/skills/grill-with-docs
```

Restart Codex after installation.

## Follow-Up Workflow

Use `elicitation-two-pass` for first-pass decision support. Use `compare-alternatives` when the user wants to know what another choice would have changed. If the user wants a deeper, document-backed decision review, follow up with `grill-with-docs`.

Use `course-correct` during active work when the next question is whether to continue, adjust, backtrack, or pause.

Use `work-harness` when the whole task should run through explicit checkpoints and final audit.

Use `grill-with-docs` when a plan needs deeper review against repository documentation and domain language.

## License

MIT License. Copyright (c) 2026 Crasnec.
