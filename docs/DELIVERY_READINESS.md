# Delivery Readiness

This document summarizes what the toolkit is ready to do, what has been validated, and what still remains outside the current release boundary.

## Current Release Status

- Release version: `0.2.0`
- Release state: provider internal beta
- Intended usage: internal provider validation and limited pilot integrations with real Android projects

## Ready Now

- Static diagnosis of Android project shape
- Detection of manifest and Gradle wiring gaps
- Detection of core USDK integration hooks
- Detection of lifecycle forwarding gaps
- Template-guided integration scaffolding
- Structured repair planning
- Explicit protocol-mode guidance
- Strong exit-logic reminder behavior
- Role-reporting skeleton coverage:
  - `enterGame`
  - `createNewRole`
  - `roleLevelUp`
- Core callback coverage:
  - init
  - login
  - switch account
  - kick/offline
  - logout
  - exit
  - pay

## Validated In This Repo

- Fixture-based validation for:
  - `fixtures/android-native-minimal`
  - `fixtures/android-partial-integration`
- Real sample-project static integration trial:
  - `D:\AndroidProjects\USDK_AI_Sample`
- Current doctor target state for validated projects:
  - fixtures:
    - `integration_partially_detected`
    - prioritized repairs populated for the newly required role-reporting and kick-listener hooks
  - real sample project:
    - `blocked_on_manual_inputs`
    - zero failed required checks

## Not In Scope Yet

- Packaging as a no-Python public distribution
- Provider console automation
- Backend callback provisioning
- Runtime smoke automation against real SDK binaries
- Channel-by-channel behavioral certification
- Optional extension-module automation outside the core path

## Known Operator Requirements

- Python 3.x on the machine running the scripts
- Access to the target Android project root
- Access to the official USDK binary package
- Access to provider-side values such as:
  - `product_id`
  - `product_key`
  - `payment_callback_url`
  - `payment_callback_key`

## Delivery Recommendation

This release is suitable for:

- provider-side internal rollout
- integration support team usage
- limited pilot delivery to selected integrators with support coverage

This release is not yet suitable for:

- self-serve public delivery with no provider support
- teams that cannot run local scripts
- environments that require zero local runtime dependencies
