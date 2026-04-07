# Action Template

Use this template after you run `usdk_doctor.py`.

## Inputs

- `doctor_result.json`
- [`spec/USDK_INTEGRATION_SPEC.yaml`](../../spec/USDK_INTEGRATION_SPEC.yaml)
- [`spec/USDK_REPAIR_PLAYBOOK.yaml`](../../spec/USDK_REPAIR_PLAYBOOK.yaml)
- [`template_index.md`](template_index.md)

## Decision Protocol

1. Read `summary.status`.
2. If status is `blocked_on_project_shape`, do not edit code. Report the path issue first.
3. Otherwise, read `prioritized_repairs`.
4. Work in this order:
   - Priority `0`: project root or module-shape blockers
   - Priority `1`: resources, variant choice, application entry, consent gate, init, login, role upload, pay
   - Priority `2`: logout, exit, lifecycle forwarding, advisory consent-path details

## Execution Rules

### Before Editing

- Reuse existing entry points instead of creating duplicates.
- Prefer editing the real `Application`, launch activity, and main activity.
- Keep provider-side values as placeholders when they are not available.
- Do not guess whether the project wants SDK-hosted consent or self-hosted consent.
- If no evidence exists, stop and present exactly two choices to the integrator:
  - `USDK protocol popup`: wire `setProtocolListener`
  - `Game-owned protocol popup`: wait for the game's own consent result, then call `setAgreeProtocol`
- Do not implement both paths as active runtime behavior in the same integration entry point. Keep the selected path active and document the other as an explicit alternative.
- Treat `exit` logic as a strong reminder, not as a separate branch choice.
- Explicitly tell the integrator to review whether the channel provides its own exit dialog, whether the game needs a local confirmation dialog when the channel does not, and which in-game actions should route through the shared exit path.

### During Editing

For each `prioritized_repairs` item:

1. Look up the `check_id` in the repair playbook.
2. Confirm the prerequisite checks or files exist.
3. Load the matching template from the template index when one exists.
4. Edit only the target files needed for that repair.
5. Preserve existing project logic and add USDK integration around it.
6. Mark any provider-side or backend dependency as a manual input, not as a code edit.

### After Each Pass

Run:

```bash
python scripts/usdk_doctor.py --project-root <target_project_root> --pretty
```

Then compare:
- `required_failed_count`
- `required_warning_count`
- `prioritized_repairs`

Stop only when:
- all statically detectable required engineering checks are green, or
- the remaining blockers are truly manual inputs or project-structure ambiguity

## Output Template

Return your final result in four buckets:

### 1. Completed

- Files updated
- Checks cleared

### 2. Remaining Repairs

- Any failed required checks still present
- Why they remain

### 3. Manual Inputs

- `product_id`
- `product_key`
- `sdk_variant`
- `protocol_popup_mode`
  - `USDK protocol popup`
  - `Game-owned protocol popup`
- `payment_callback_url`
- `payment_callback_key`

### 4. Assumptions And Risks

- Which consent path was assumed
- Whether exit logic was explicitly called out to the integrator as a runtime review item
- Whether the project shape was adapted rather than matching the canonical sample
- Any areas where runtime verification is still required
