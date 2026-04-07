# Android Partial Integration Fixture

This fixture represents a project that has started USDK integration but is still missing major required runtime and lifecycle wiring.

Use it like this:

```bash
python scripts/usdk_doctor.py --project-root fixtures/android-partial-integration --pretty
```

Expected result shape:
- `project_type = android_native`
- `detected_sdk_variant = android`
- `summary.status = integration_partially_detected`
- multiple failed `required` checks with populated `prioritized_repairs`
