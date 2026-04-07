Perform USDK Android engineering integration work for the current project using the vendored toolkit at `tools/usdk-android-ai-integration-toolkit`.

Required steps:

1. Read:
   - `tools/usdk-android-ai-integration-toolkit/spec/USDK_INTEGRATION_SPEC.yaml`
   - `tools/usdk-android-ai-integration-toolkit/spec/USDK_REPAIR_PLAYBOOK.yaml`
   - `tools/usdk-android-ai-integration-toolkit/skill/usdk-android-integration/references/action_template.md`
   - `tools/usdk-android-ai-integration-toolkit/skill/usdk-android-integration/references/template_index.md`
   - `tools/usdk-android-ai-integration-toolkit/skill/usdk-android-integration/references/manual_inputs.md`
2. Run the doctor before editing:
   - `python tools/usdk-android-ai-integration-toolkit/scripts/usdk_doctor.py --project-root . --pretty`
3. Run the repair runner if the repair set is non-trivial:
   - `python tools/usdk-android-ai-integration-toolkit/scripts/usdk_repair_runner.py --project-root . --format markdown`
4. Confirm required human decisions instead of guessing them:
   - protocol mode
   - exit-path logic
   - provider and backend values
5. Apply additive edits.
6. Re-run the doctor after editing.
7. Report:
   - completed work
   - remaining manual inputs
   - risks and assumptions

When implementing `exit(activity)`, explicitly remind the integrator:

- If the channel provides an exit dialog, the game must not show an extra local exit confirmation dialog.
- If the channel does not provide an exit dialog, the game must show its own local confirmation before calling `exit(activity)`.
- The integrator must confirm which user actions share the exit path.

If the user provided extra instructions, apply them as additional scope: `$ARGUMENTS`
