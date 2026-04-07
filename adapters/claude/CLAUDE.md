# USDK Android Integration Memory For Claude Code

Use this file in a target Android project that vendors the toolkit at:

`tools/usdk-android-ai-integration-toolkit`

## Read First

- `tools/usdk-android-ai-integration-toolkit/spec/USDK_INTEGRATION_SPEC.yaml`
- `tools/usdk-android-ai-integration-toolkit/spec/USDK_REPAIR_PLAYBOOK.yaml`
- `tools/usdk-android-ai-integration-toolkit/skill/usdk-android-integration/references/action_template.md`
- `tools/usdk-android-ai-integration-toolkit/skill/usdk-android-integration/references/template_index.md`
- `tools/usdk-android-ai-integration-toolkit/skill/usdk-android-integration/references/manual_inputs.md`

## Required Workflow

1. Run the doctor before editing:

`python tools/usdk-android-ai-integration-toolkit/scripts/usdk_doctor.py --project-root . --pretty`

2. If the repair set is non-trivial, run the phased planner:

`python tools/usdk-android-ai-integration-toolkit/scripts/usdk_repair_runner.py --project-root . --format markdown`

3. Apply changes using the diagnosis and repair playbook as the source of truth.
4. Re-run the doctor after edits.
5. Report completed work, remaining manual inputs, and risks.

## Do Not Guess

- protocol mode
- exit-path product logic
- provider console values
- backend callback values
- real `RoleInfo` field mappings
- real `OrderInfo` field mappings

## Project Commands

If this project also copies the bundled Claude project commands, you can use:

- `/usdk-diagnose`
- `/usdk-plan`
- `/usdk-integrate`

If the toolkit is vendored in another location, update this file and the copied project commands before use.
