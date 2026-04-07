# USDK Android AI Integration Toolkit Memory

This repository is the source repository for the USDK Android AI Integration Toolkit.

## Use This Repository For

- maintaining the toolkit itself
- validating bundled doctor and repair-runner behavior
- preparing adapter assets for other AI coding tools

## Integration Backend

When using this toolkit against a real Android project, the execution backend is:

- `spec/USDK_INTEGRATION_SPEC.yaml`
- `spec/USDK_REPAIR_PLAYBOOK.yaml`
- `scripts/usdk_doctor.py`
- `scripts/usdk_repair_runner.py`
- `skill/usdk-android-integration/references/`

## Required Operating Sequence

1. Read the spec and repair playbook.
2. Run the doctor against the target project before editing.
3. Run the repair runner when the repair set is non-trivial.
4. Apply additive changes where possible.
5. Re-run the doctor after editing.
6. Report completed work, remaining manual inputs, and risks.

## Never Guess These Decisions

- protocol mode choice
- exit-path product logic
- provider console values
- backend callback values
- real role and order field mappings

## Adapter Templates

Portable templates for other AI coding tools live under:

- `adapters/cursor/`
- `adapters/claude/`

They assume the toolkit is vendored into the target project at:

`tools/usdk-android-ai-integration-toolkit`

If a target project uses another location, update the copied template paths first.
