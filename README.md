# elicitation-two-pass

Codex skill for decision support on high-impact, underspecified requests.

The skill helps Codex separate:

- baseline controls that should be handled directly
- material user-owned decisions and tradeoffs
- facts needed before finalizing
- external checks for current, local, regulated, proprietary, or specialist details
- validation steps for the riskiest assumptions

## Repository Layout

```text
skills/
  elicitation-two-pass/
    SKILL.md
    agents/
      openai.yaml
```

## Install From GitHub

After publishing this repository, install the skill by pointing Codex's skill installer at the skill path:

```bash
python3 /home/adjustedmin/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo <owner>/<repo> \
  --path skills/elicitation-two-pass
```

Or use a GitHub URL:

```bash
python3 /home/adjustedmin/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --url https://github.com/<owner>/<repo>/tree/main/skills/elicitation-two-pass
```

Restart Codex after installation.

## Follow-Up Workflow

Use this skill for first-pass decision support. If the user wants a deeper, document-backed decision review, follow up with `grill-with-docs`.
