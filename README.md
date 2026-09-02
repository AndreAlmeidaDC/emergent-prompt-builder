# emergent-prompt-builder

Workflow skill for the current Emergent platform.

The legacy edition described a fixed five-agent team, a fixed MongoDB stack for every project, no more than four prompts per phase and a two-attempt stop rule. The new version selects the current agent according to the job, plans in manageable slices, measures convergence by new evidence, uses GitHub/forking/savepoints and separates agent output from independent verification.

## Core sequence

```text
inspect -> choose agent/autonomy -> contract -> phase -> evidence checkpoint -> verify -> approved release
```

## Verification

```bash
python3 scripts/validate_skill.py
```

Version `2026.09.02` is a breaking replacement of the fixed-team workflow.
