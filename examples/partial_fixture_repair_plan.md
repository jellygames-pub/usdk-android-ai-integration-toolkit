# USDK Repair Plan

- Project root: `C:\Users\Administrator\Documents\New project\fixtures\android-partial-integration`
- Project type: `android_native`
- Doctor status: `integration_partially_detected`

Use the phased repair plan to clear the remaining static integration issues.

## Phases

### Application And Splash Entry

Edit scope:
- `Application class`
- `app/src/main/AndroidManifest.xml`
- `Splash or launch activity`
Templates:
- `skill/usdk-android-integration/references/templates/application_java.md`
- `skill/usdk-android-integration/references/templates/splash_activity_java.md`
Repairs:
- `application_extends_sdkapplication`: Update the owning Application class to extend SdkApplication and wire that class through the manifest.
- `manifest_application_name_present`: Declare the owning Application class in AndroidManifest.xml so USDK can attach through the intended application entry point.
- `splash_extends_sdksplashactivity`: Attach USDK splash integration by making the launch splash activity extend SdkSplashActivity.

### Consent And Runtime Chain

Edit scope:
- `Role entry point`
- `main game activity`
- `Splash or launch activity`
- `integration wrapper`
- `Purchase flow owner`
- `consent flow owner`
- `Exit flow owner`
- `Account or session owner`
Templates:
- `skill/usdk-android-integration/references/templates/runtime_chain_java.md`
- `skill/usdk-android-integration/references/templates/splash_activity_java.md`
Repairs:
- `enter_game_call_present`: Upload role data with enterGame after login succeeds and real role data is available.
- `init_call_present`: Add the HeroSdk init call to the runtime chain after protocol consent.
- `pay_call_present`: Add the HeroSdk pay call to the real purchase flow with OrderInfo and RoleInfo.
- `runtime_protocol_gate_present`: Make init happen only after protocol consent, either through setProtocolListener or through setAgreeProtocol in your own consent flow.
- `agree_protocol_present`: If you use self-hosted consent UI, call setAgreeProtocol after the user accepts the protocol.
- `exit_call_present`: Wire the USDK exit call into the game exit path after checking whether the channel owns the exit dialog.
- `logout_call_present`: Wire logout handling so the game can return to the correct post-logout state.
- `protocol_listener_present`: If you use SDK-hosted consent UI, set an IProtocolListener before calling init.

### Lifecycle Forwarding

Edit scope:
- `Main activity or integration wrapper`
Templates:
- `skill/usdk-android-integration/references/templates/activity_lifecycle_forwarding_java.md`
Repairs:
- `lifecycle_onactivityresult_forwarded`: Forward Activity onActivityResult into HeroSdk.
- `lifecycle_ondestroy_forwarded`: Forward Activity onDestroy into HeroSdk.
- `lifecycle_onnewintent_forwarded`: Forward Activity onNewIntent into HeroSdk.
- `lifecycle_onpause_forwarded`: Forward Activity onPause into HeroSdk.
- `lifecycle_onrequestpermissionsresult_forwarded`: Forward Activity onRequestPermissionsResult into HeroSdk.
- `lifecycle_onrestart_forwarded`: Forward Activity onRestart into HeroSdk.
- `lifecycle_onresume_forwarded`: Forward Activity onResume into HeroSdk.
- `lifecycle_onstart_forwarded`: Forward Activity onStart into HeroSdk.
- `lifecycle_onstop_forwarded`: Forward Activity onStop into HeroSdk.

## Manual Inputs

- `product_id`
- `product_key`
- `sdk_variant`
- `protocol_popup_mode`
- `payment_callback_url`
- `payment_callback_key`

## Assumptions

- Use legacy support-oriented Gradle templates unless the target project is being migrated.
- Choose one consent path before wiring init: SDK-hosted or self-hosted.

