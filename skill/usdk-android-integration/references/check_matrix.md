# Doctor Check Matrix

The first-pass doctor emits these check ids.

## Project Checks

- `android_project_detected`
- `android_manifest_found`
- `app_gradle_found`

## Resource Checks

- `hero_aar_present`
- `herosdkcfg_present`
- `herosdkcfg_has_product_placeholders`

## Manifest Checks

- `manifest_install_location_auto`
- `manifest_application_declared`
- `manifest_application_name_present`

## Gradle Checks

- `gradle_flatdir_present`
- `gradle_herousdk_dependency_present`
- `gradle_sdk_variant_detected`

## Code Hook Checks

- `application_extends_sdkapplication`
- `splash_extends_sdksplashactivity`
- `protocol_listener_present`
- `agree_protocol_present`
- `init_call_present`
- `login_call_present`
- `enter_game_call_present`
- `create_new_role_call_present`
- `role_level_up_call_present`
- `pay_call_present`
- `kick_listener_present`
- `logout_call_present`
- `exit_call_present`
- `runtime_protocol_gate_present`

## Lifecycle Checks

- `lifecycle_oncreate_forwarded`
- `lifecycle_onnewintent_forwarded`
- `lifecycle_onstart_forwarded`
- `lifecycle_onresume_forwarded`
- `lifecycle_onpause_forwarded`
- `lifecycle_onstop_forwarded`
- `lifecycle_onrestart_forwarded`
- `lifecycle_ondestroy_forwarded`
- `lifecycle_onactivityresult_forwarded`
- `lifecycle_onrequestpermissionsresult_forwarded`

## Interpretation

- `passed`: statically detected
- `warning`: pattern may be partial or ambiguous
- `failed`: expected and not found
- `not_applicable`: project shape does not support the check
