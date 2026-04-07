---
name: usdk-android-integration
description: Use this skill when integrating Hero USDK into an Android game project, auditing an existing USDK integration, or upgrading a project to the official USDK integration flow. It provides the workflow for scanning the project, classifying the integration state, applying required Android changes, and validating the result with the bundled doctor script and structured spec.
---

# USDK Android Integration

Use this skill for engineering-level USDK integration work in Android projects.

## What To Load First

1. Read [`spec/USDK_INTEGRATION_SPEC.yaml`](../../spec/USDK_INTEGRATION_SPEC.yaml).
2. Read [`spec/USDK_REPAIR_PLAYBOOK.yaml`](../../spec/USDK_REPAIR_PLAYBOOK.yaml).
3. Run [`scripts/usdk_doctor.py`](../../scripts/usdk_doctor.py) against the target project root.
4. Run [`scripts/usdk_repair_runner.py`](../../scripts/usdk_repair_runner.py) when you want a phased repair plan from the doctor result.
5. Read [`references/action_template.md`](references/action_template.md) before editing.
6. Read [`references/template_index.md`](references/template_index.md) when you start applying repairs.
7. Read [`references/manual_inputs.md`](references/manual_inputs.md) if required inputs are missing.
8. Read [`references/check_matrix.md`](references/check_matrix.md) when you need the exact meaning of a doctor check.

## Workflow

1. Classify the project.
   Supported first-pass targets:
   - Native Android Studio app projects
   - Android game shells exported from Unity or similar engines, as long as they still contain Android app/module files

2. Collect facts before editing.
   Run:
   ```bash
   python scripts/usdk_doctor.py --project-root <target_project_root>
   ```
   Use the JSON result as the source of truth for current status and repair order.
   If the repair set is large, then run:
   ```bash
   python scripts/usdk_repair_runner.py --project-root <target_project_root> --format markdown
   ```
   Use the phase plan to drive edit order.

3. Decide scope.
   Required integration path in this first version:
   - Resource presence and config files
   - `Application` integration
   - `SplashActivity` integration
   - `AndroidManifest.xml` required items
   - `build.gradle` USDK dependency and local libs wiring
   - Core runtime chain: protocol -> init -> login -> enterGame -> pay -> logout/exit
   - Activity lifecycle forwarding

4. Apply changes carefully.
   Rules:
   - Do not overwrite unrelated game logic.
   - Prefer additive edits.
   - If the project already has a custom integration wrapper, adapt to it instead of forcing a second wrapper.
   - Treat `productId`, `productKey`, goods config, callback URLs, and backend settings as external inputs unless they already exist in the project.
   - Use `prioritized_repairs` from the doctor result to choose the next edit.
   - Use the repair playbook entry for each failed check before writing code.

5. Re-run validation.
   After edits, run the doctor again and compare results.
   The goal is:
   - No failed required engineering checks that can be detected statically
   - Clear list of manual follow-ups that require provider or backend action

6. Report in three buckets.
   - Completed
   - Remaining manual inputs
   - Risks or assumptions

## Editing Guidance

### Required Order

1. Protocol handling
2. SDK init
3. Login and account callbacks, including kick/offline handling
4. Role upload hooks, including `enterGame`, `createNewRole`, and `roleLevelUp`
5. Payment hook
6. Logout and exit
7. Lifecycle forwarding

### Do Not Assume

- Real `productId` or `productKey`
- Real payment callback URL
- Whether the project wants SDK-hosted protocol UI or self-hosted protocol UI
- Whether optional extensions are enabled
- Whether the target package is domestic official, global, market, or another bundle mode

Before implementing protocol handling, present the integrator with exactly two choices:
- `USDK protocol popup`: use `setProtocolListener`
- `Game-owned protocol popup`: use the game's own popup, then call `setAgreeProtocol`

When implementing exit integration, explicitly remind the integrator:
- whether the channel provides its own exit dialog
- whether the game must show its own exit confirmation when the channel does not
- which game actions should route through the shared exit path, including the back key when applicable

### When To Stop And Escalate

Stop and ask for confirmation if:
- The project is not a recognizable Android app/module layout
- There are multiple competing `Application` classes and the safe owner is unclear
- The app uses a generated manifest or build system that would make direct file edits fragile
- The project mixes legacy support libraries and AndroidX in a way that makes the USDK variant choice unclear

## Deliverables

For each integration task, produce:
- Updated project files
- A doctor result before and after
- The remaining manual inputs required to finish the integration
