# Integrator Quickstart

This guide is for integrators or AI operators using the USDK Android toolkit against a real project.

## Inputs You Need

- Target Android project root
- Official USDK package files
- Python 3.x on the machine running the toolkit scripts
- Provider-side values:
  - `product_id`
  - `product_key`
  - `sdk_variant`
  - `protocol_popup_mode`
  - `payment_callback_url`
  - `payment_callback_key`

## What AI Will Not Guess

- Protocol mode:
  - `USDK protocol popup`
  - `Game-owned protocol popup`
- Exit logic:
  - AI must call out the channel exit-dialog logic and the game-local exit logic as a runtime review item
- Role-reporting field mapping:
  - AI can scaffold `RoleInfo`, but it cannot invent the real game-side field mapping
- Payment field mapping:
  - AI can scaffold `OrderInfo`, but it cannot invent the real goods, order, and callback data

## Recommended Flow

1. Put the toolkit next to your working environment.
2. Run the doctor:

   ```bash
   python scripts/usdk_doctor.py --project-root <android_project_root> --pretty
   ```

3. If there are many missing checks, generate a repair plan:

   ```bash
   python scripts/usdk_repair_runner.py --project-root <android_project_root> --format markdown
   ```

4. Load the skill and supporting files into your AI tool:
   - `skill/usdk-android-integration/SKILL.md`
   - `spec/USDK_INTEGRATION_SPEC.yaml`
   - `spec/USDK_REPAIR_PLAYBOOK.yaml`

5. Let the AI apply engineering changes phase by phase.
6. Re-run the doctor after each pass.
7. Stop when the status reaches `blocked_on_manual_inputs` or better.

## Gradle Repository Note

- For Gradle 7+ projects that manage repositories from `settings.gradle`, declare the local `flatDir` repository in `settings.gradle`.
- For older projects that still allow module-level repositories, declaring `flatDir` in `app/build.gradle` is still acceptable.

## Expected End State

The target project should reach:

- No failed required static engineering checks
- A short list of provider-side manual inputs still needed
- A clear runtime validation follow-up list

## Common Interpretation

- `blocked_on_project_shape`
  The toolkit is pointed at the wrong root or the project layout is unsupported.

- `integration_partially_detected`
  USDK work has started but major engineering hooks are still missing.

- `blocked_on_manual_inputs`
  Static engineering work is complete enough. Remaining work is provider-side parameters, backend setup, and runtime verification.

- `integration_verified_static`
  All detectable static checks are green and no outstanding manual blockers were declared.
