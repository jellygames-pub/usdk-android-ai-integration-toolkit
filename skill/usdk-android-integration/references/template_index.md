# Template Index

Load these templates only when the related repair is active.

## App Entry

- [`templates/application_java.md`](templates/application_java.md)
  Use when fixing:
  - `application_extends_sdkapplication`
  - `manifest_application_name_present`

- [`templates/splash_activity_java.md`](templates/splash_activity_java.md)
  Use when fixing:
  - `splash_extends_sdksplashactivity`
  - `protocol_listener_present`
  - `agree_protocol_present`
  - `runtime_protocol_gate_present`
  - `init_call_present`

## Runtime

- [`templates/runtime_chain_java.md`](templates/runtime_chain_java.md)
  Use when fixing:
  - `login_call_present`
  - `enter_game_call_present`
  - `pay_call_present`
  - `logout_call_present`
  - `exit_call_present`

## Lifecycle

- [`templates/activity_lifecycle_forwarding_java.md`](templates/activity_lifecycle_forwarding_java.md)
  Use when fixing:
  - all `lifecycle_*` checks

## Gradle And Config

- [`templates/gradle_androidx.md`](templates/gradle_androidx.md)
  Use when fixing:
  - `gradle_flatdir_present`
  - `gradle_herousdk_dependency_present`
  - `gradle_sdk_variant_detected` for AndroidX projects

- [`templates/gradle_legacy_android.md`](templates/gradle_legacy_android.md)
  Use when fixing:
  - `gradle_flatdir_present`
  - `gradle_herousdk_dependency_present`
  - `gradle_sdk_variant_detected` for legacy support projects
