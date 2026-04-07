Create a phased USDK integration repair plan for the current Android project using the vendored toolkit at `tools/usdk-android-ai-integration-toolkit`.

Required steps:

1. Read:
   - `tools/usdk-android-ai-integration-toolkit/spec/USDK_INTEGRATION_SPEC.yaml`
   - `tools/usdk-android-ai-integration-toolkit/spec/USDK_REPAIR_PLAYBOOK.yaml`
   - `tools/usdk-android-ai-integration-toolkit/skill/usdk-android-integration/references/action_template.md`
2. Run:
   - `python tools/usdk-android-ai-integration-toolkit/scripts/usdk_doctor.py --project-root . --pretty`
   - `python tools/usdk-android-ai-integration-toolkit/scripts/usdk_repair_runner.py --project-root . --format markdown`
3. Return:
   - phased repair order
   - files likely to change
   - manual confirmations required before editing

If the user provided extra instructions, apply them as additional scope: `$ARGUMENTS`
