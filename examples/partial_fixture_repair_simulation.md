# Partial Fixture Repair Simulation

This example shows how AI should interpret the doctor output for the partial fixture.

## Input

Command:

```bash
python scripts/usdk_doctor.py --project-root fixtures/android-partial-integration --pretty
```

Observed high-priority repairs:

1. `application_extends_sdkapplication`
2. `splash_extends_sdksplashactivity`
3. `runtime_protocol_gate_present`
4. `init_call_present`
5. `enter_game_call_present`
6. `pay_call_present`

## Planned Edit Order

### Pass 1

- Add an `Application` class that extends `SdkApplication`
- Update `AndroidManifest.xml` to point `android:name` at that class
- Convert the launcher activity or a new splash owner into `SdkSplashActivity`
- Add one consent path and gate `init` behind it

Expected outcome:
- clear `manifest_application_name_present`
- clear `application_extends_sdkapplication`
- clear `splash_extends_sdksplashactivity`
- clear `runtime_protocol_gate_present`
- clear `init_call_present`

### Pass 2

- Add role upload and payment hooks in the real runtime owner
- Add logout and exit hooks if the project has those surfaces

Expected outcome:
- clear `enter_game_call_present`
- clear `pay_call_present`
- reduce runtime failures

### Pass 3

- Forward the missing lifecycle callbacks from the main activity

Expected outcome:
- clear all `lifecycle_*` failures

## Example AI Summary

Completed:
- Connected Application ownership to `SdkApplication`
- Added splash integration and consent-gated `init`

Remaining repairs:
- Runtime purchase and role upload hooks still need to be attached to the real gameplay flow
- Missing lifecycle forwarding still blocks static verification

Manual inputs:
- `product_id`
- `product_key`
- `protocol_popup_mode`
- `payment_callback_url`
- `payment_callback_key`

Assumptions:
- SDK-hosted consent path was chosen for the simulation
- Launcher activity was treated as the splash owner because the fixture did not contain a separate splash class
