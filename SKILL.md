---
name: emergent-prompt-builder
description: >
  Guides planning, building, repairing, testing and releasing web or mobile products with the current Emergent agents. Use when the user mentions Emergent, E1/E1.5/E2, Prototype, Mobile Agent, Emergent GitHub, forking, MCP, custom agents or asks for structured Emergent prompts. Choose agent and autonomy according to the task, then control convergence, cost and release risk.
license: MIT
---

# Emergent Prompt Builder

This skill treats Emergent as an agentic development platform with selectable main agents, focused sub-agents, GitHub, testing, deployment, forking, MCP and mobile workflows. It does not freeze the platform into a fictional fixed team or arbitrary prompt-count rules.

## Origin version check

Canonical source:

```text
https://github.com/AndreAlmeidaDC/emergent-prompt-builder
```

At meaningful use, follow `references/version-check.md`. Never self-update silently.

## Load order

1. Read `references/vibecode-core.md`.
2. Read `references/platform-emergent.md`.
3. Use `references/archetypes.md` only when platform choice is open.
4. Select the smallest agent and autonomy profile that protects quality.

## Non-negotiable boundaries

- Verify current agent availability and project state before recommending a model.
- Define stop/escalation conditions; never count retries blindly.
- Keep GitHub/savepoints and rollback current during long runs.
- Review code and tests independently from the producing agent when risk is material.
- Do not paste secrets into prompts or let agents perform payment, production, public communication or destructive actions without explicit approval.
- Treat credits, plans, context limits and model names as volatile claims.

## Output

Return only what is needed: agent-selection memo, project brief, phase plan, atomic follow-up, convergence checkpoint, reanchoring prompt, verification prompt or release checklist.

## Change history

| Date | Version | Change |
|---|---|---|
| 2026-09-02 | 2026.09.02 | Rebuilt for selectable Emergent agents, context/forking, GitHub, MCP, mobile, convergence control, independent verification and volatile cost claims. |
