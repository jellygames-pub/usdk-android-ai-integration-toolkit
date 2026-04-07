# USDK Provider Workflow

This repository is the packaged provider toolkit for AI-guided USDK Android integration.

## Goal

Give integrators and AI tools one official path:

1. Read the structured spec.
2. Diagnose the current project with the doctor script.
3. Apply engineering changes with the skill workflow.
4. Re-run diagnosis.
5. Separate code-complete work from provider-side manual inputs.

## Release

- Current version: `0.2.0`
- Release state: provider internal beta
- Top-level entrypoint: [README.md](../README.md)
- Integrator entrypoint: [INTEGRATOR_QUICKSTART.md](INTEGRATOR_QUICKSTART.md)
- Delivery readiness: [DELIVERY_READINESS.md](DELIVERY_READINESS.md)
- Provider release checklist: [PROVIDER_RELEASE_CHECKLIST.md](PROVIDER_RELEASE_CHECKLIST.md)
- Runtime requirement for scripts: Python 3.x

## Roles

### Provider

- Maintains the skill
- Maintains the structured integration spec
- Maintains the doctor script and output schema
- Owns versioning and rule updates

### Integrator

- Runs the doctor script inside the target project
- Uses the skill or AI workflow to apply engineering changes
- Supplies real product and payment configuration values
- Completes runtime and backend validation

### AI Tool

- Reads the spec
- Runs the doctor script before editing
- Uses doctor output to decide what to change
- Re-runs the doctor after editing
- Reports completed work and manual blockers separately

## Recommended Integrator Flow

1. Unpack or clone this toolkit.
2. Put the target Android project path in `--project-root`.
3. Run:
   ```bash
   python scripts/usdk_doctor.py --project-root <android_project_root> --pretty
   ```
4. Optionally generate a phased repair plan:
   ```bash
   python scripts/usdk_repair_runner.py --project-root <android_project_root> --format markdown
   ```
5. Feed the output plus the skill, integration spec, and repair playbook into the AI tool.
6. Let the AI apply the required integration changes.
7. Re-run the doctor and compare the result.
8. Finish remaining provider and backend items.

The doctor now emits both:
- `checks`: the full structured result
- `prioritized_repairs`: the first things AI or an integrator should change, sorted by priority
- `phase_plan`: a runner-generated grouped repair plan for larger integration gaps

## First-Pass Deliverables In This Repo

- `skill/usdk-android-integration/SKILL.md`
- `spec/USDK_INTEGRATION_SPEC.yaml`
- `spec/USDK_REPAIR_PLAYBOOK.yaml`
- `scripts/usdk_doctor.py`
- `scripts/usdk_repair_runner.py`
- `skill/usdk-android-integration/references/action_template.md`
- `skill/usdk-android-integration/references/template_index.md`
- `skill/usdk-android-integration/references/check_matrix.md`
- `skill/usdk-android-integration/references/manual_inputs.md`
- `fixtures/android-native-minimal/`
- `docs/AI_COMPATIBILITY.md`
- `docs/DELIVERY_READINESS.md`
- `docs/PROVIDER_RELEASE_CHECKLIST.md`

## Template Layer

The provider toolkit now includes reusable template references for:
- Application integration
- Splash and consent integration
- Runtime login, role upload, payment, logout, and exit hooks
- Activity lifecycle forwarding
- Gradle wiring for AndroidX and legacy support paths

These templates are not meant to be pasted blindly. AI should load the smallest matching template, adapt it to the host project, and preserve existing logic.

## Fixture Validation

Use the included fixture to sanity-check doctor behavior during provider-side iteration:

```bash
python scripts/usdk_doctor.py --project-root fixtures/android-native-minimal --pretty
python scripts/usdk_doctor.py --project-root fixtures/android-partial-integration --pretty
```

Expected result shape:
- `project_type = android_native`
- `detected_sdk_variant = androidx`
- `summary.status = integration_partially_detected`
- failed `required` checks should specifically reflect the missing role-reporting and kick-listener coverage in the fixture

For the partial fixture:
- `project_type = android_native`
- `detected_sdk_variant = android`
- `summary.status = integration_partially_detected`
- `prioritized_repairs` should be populated with actionable items

The fixture is intentionally static-only. It exists to validate detection rules, not to build or run.

## Next Iteration Suggestions

- Add project fixtures for more real app shapes
- Add more precise Gradle and Manifest parsing
- Add optional extension-module checks
- Add provider console export support or MCP only after the static path is stable
- Add a no-Python delivery format only after the internal beta path is stable
