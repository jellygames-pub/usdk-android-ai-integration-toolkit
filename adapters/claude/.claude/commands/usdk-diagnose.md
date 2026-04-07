Diagnose the current Android project for USDK integration using the vendored toolkit at `tools/usdk-android-ai-integration-toolkit`.

Required steps:

1. Read:
   - `tools/usdk-android-ai-integration-toolkit/spec/USDK_INTEGRATION_SPEC.yaml`
   - `tools/usdk-android-ai-integration-toolkit/spec/USDK_REPAIR_PLAYBOOK.yaml`
2. Run:
   - `python tools/usdk-android-ai-integration-toolkit/scripts/usdk_doctor.py --project-root . --pretty`
3. Summarize the result in three buckets:
   - completed checks
   - failed or warning checks
   - remaining manual inputs

If the user provided extra instructions, apply them as additional scope: `$ARGUMENTS`
