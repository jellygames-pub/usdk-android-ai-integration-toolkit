# USDK Repair Plan

- Project root: `C:\Users\Administrator\Documents\New project\fixtures\android-partial-integration`
- Project type: `android_native`
- Doctor status: `blocked_on_manual_inputs`

Static engineering checks are clear. Remaining work is provider-side manual input and runtime verification.

## Phases

### Consent And Runtime Chain

Edit scope:
- `Splash or launch activity`
- `consent flow owner`
Templates:
- `skill/usdk-android-integration/references/templates/splash_activity_java.md`
Repairs:
- `agree_protocol_present`: If you use self-hosted consent UI, call setAgreeProtocol after the user accepts the protocol.

## Manual Inputs

- `product_id`
- `product_key`
- `sdk_variant`
- `protocol_popup_mode`
- `payment_callback_url`
- `payment_callback_key`

## Assumptions

- Use legacy support-oriented Gradle templates unless the target project is being migrated.

