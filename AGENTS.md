# USDK Android AI Integration Toolkit Agent Guide

Use this repository as the source of truth when adapting AI coding agents for USDK Android integration.

## Scope

- This repository is the toolkit source repository.
- When integrating a real Android game project, prefer vendoring this toolkit into the target project and then using the adapter templates in `adapters/`.
- Do not assume the target project already contains USDK-specific wrappers or complete runtime hooks.

## Read First

1. `spec/USDK_INTEGRATION_SPEC.yaml`
2. `spec/USDK_REPAIR_PLAYBOOK.yaml`
3. `skill/usdk-android-integration/references/action_template.md`
4. `skill/usdk-android-integration/references/template_index.md`
5. `skill/usdk-android-integration/references/manual_inputs.md`

## Required Workflow

1. Diagnose before editing.
   - Run `python scripts/usdk_doctor.py --project-root <target_project_root> --pretty`
2. Generate a phased repair plan when the diagnosis is not already clean.
   - Run `python scripts/usdk_repair_runner.py --project-root <target_project_root> --format markdown`
3. Apply only the repairs justified by the diagnosis and playbook.
4. Re-run the doctor after edits.
5. Report:
   - completed engineering work
   - remaining manual inputs
   - assumptions or risks

## Human Confirmations You Must Not Guess

- Protocol mode:
  - `USDK protocol popup`
  - `Game-owned protocol popup`
- Exit logic reminder:
  - whether the channel provides its own exit dialog
  - whether the game must show its own local confirmation when the channel does not
  - which game actions must route through the shared exit path
- Real provider and backend values:
  - `productId`
  - `productKey`
  - payment callback configuration
  - real `RoleInfo` field mapping
  - real `OrderInfo` field mapping

## Adapter Assets

- Cursor adapter templates: `adapters/cursor/`
- Claude Code adapter templates: `adapters/claude/`

Use these templates when preparing a target project for Cursor or Claude Code. The recommended layout is:

```text
<game-project>/
  tools/usdk-android-ai-integration-toolkit/
  AGENTS.md
  CLAUDE.md
  .cursor/rules/
  .claude/commands/
```

If the vendored toolkit path differs from `tools/usdk-android-ai-integration-toolkit`, update the copied adapter files before use.
