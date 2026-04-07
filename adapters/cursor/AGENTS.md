# USDK Android Integration Instructions For Cursor

Use these instructions in a target Android project that vendors this toolkit at:

`tools/usdk-android-ai-integration-toolkit`

## Read First

1. `tools/usdk-android-ai-integration-toolkit/spec/USDK_INTEGRATION_SPEC.yaml`
2. `tools/usdk-android-ai-integration-toolkit/spec/USDK_REPAIR_PLAYBOOK.yaml`
3. `tools/usdk-android-ai-integration-toolkit/skill/usdk-android-integration/references/action_template.md`
4. `tools/usdk-android-ai-integration-toolkit/skill/usdk-android-integration/references/template_index.md`
5. `tools/usdk-android-ai-integration-toolkit/skill/usdk-android-integration/references/manual_inputs.md`

## Required Workflow

1. Diagnose the current project before editing:

```bash
python tools/usdk-android-ai-integration-toolkit/scripts/usdk_doctor.py --project-root . --pretty
```

2. If the diagnosis shows multiple required repairs, generate a phased plan:

```bash
python tools/usdk-android-ai-integration-toolkit/scripts/usdk_repair_runner.py --project-root . --format markdown
```

3. Apply only the changes supported by the diagnosis, repair playbook, and template references.
4. Re-run the doctor after edits.
5. Report:
   - completed engineering items
   - remaining manual inputs
   - assumptions and risks

## Do Not Guess

- protocol mode:
  - `USDK protocol popup`
  - `Game-owned protocol popup`
- exit-path product logic
- provider console values
- backend callback values
- real `RoleInfo` field mappings
- real `OrderInfo` field mappings

## Exit Logic Reminder

When implementing `exit(activity)`, explicitly remind the integrator:

- If the channel provides an exit dialog, the game must not show an extra local exit confirmation dialog.
- If the channel does not provide an exit dialog, the game must show its own local confirmation before calling `exit(activity)`.
- The integrator must confirm which user actions share the exit path, including the back key when applicable.

If the toolkit is vendored somewhere other than `tools/usdk-android-ai-integration-toolkit`, update every path in this file and in `.cursor/rules/usdk-android-integration.mdc`.
