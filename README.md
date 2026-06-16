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

Install both:

```bash
python3 /home/adjustedmin/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo Crasnec/skills \
  --path skills/elicitation-two-pass \
  --path skills/compare-alternatives
```

Or use a GitHub URL:

```bash
python3 /home/adjustedmin/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --url https://github.com/Crasnec/skills/tree/main/skills/compare-alternatives
```

Restart Codex after installation.

## Follow-Up Workflow

Use `elicitation-two-pass` for first-pass decision support. Use `compare-alternatives` when the user wants to know what another choice would have changed. If the user wants a deeper, document-backed decision review, follow up with `grill-with-docs`.
