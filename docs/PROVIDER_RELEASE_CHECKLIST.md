# Provider Release Checklist

Use this checklist before handing a toolkit build to internal integration support or pilot integrators.

## Versioning

- Update [VERSION](../VERSION)
- Update [CHANGELOG.md](../CHANGELOG.md)
- Update [toolkit-manifest.json](../toolkit-manifest.json)

## Documentation

- Confirm [README.md](../README.md) matches the current release scope
- Confirm [INTEGRATOR_QUICKSTART.md](INTEGRATOR_QUICKSTART.md) matches the current operator flow
- Confirm [USDK_PROVIDER_WORKFLOW.md](USDK_PROVIDER_WORKFLOW.md) matches the current release version
- Confirm [AI_COMPATIBILITY.md](AI_COMPATIBILITY.md) matches the current support model
- Confirm [DELIVERY_READINESS.md](DELIVERY_READINESS.md) matches the current release boundary

## Skill And Specs

- Confirm [skill/usdk-android-integration/SKILL.md](../skill/usdk-android-integration/SKILL.md) matches the current workflow
- Confirm [spec/USDK_INTEGRATION_SPEC.yaml](../spec/USDK_INTEGRATION_SPEC.yaml) matches the current required hooks
- Confirm [spec/USDK_REPAIR_PLAYBOOK.yaml](../spec/USDK_REPAIR_PLAYBOOK.yaml) matches the doctor output and template behavior

## Scripts

- Run:
  - `python -m py_compile scripts/usdk_doctor.py`
  - `python -m py_compile scripts/usdk_repair_runner.py`
- Verify `usdk_doctor.py` still reaches the expected states on bundled fixtures
- Verify `usdk_repair_runner.py` still produces phased repair output

## Fixtures

- Validate `fixtures/android-native-minimal`
- Validate `fixtures/android-partial-integration`
- Confirm the expected statuses in [toolkit-manifest.json](../toolkit-manifest.json) still match reality
- If doctor checks are expanded, update fixture expectations or fixture contents in the same release

## Sample Project Trial

- Confirm the latest real sample integration trial is still documented
- Confirm the sample project reached:
  - `blocked_on_manual_inputs`
  - zero failed required checks

## Critical Release Review

- Confirm protocol mode is still treated as an explicit integrator choice
- Confirm exit logic is still treated as a strong reminder rather than a new branch type
- Confirm role-reporting coverage still includes:
  - `enterGame`
  - `createNewRole`
  - `roleLevelUp`
- Confirm callback coverage still includes `setKickListener`
- Confirm Gradle 7+ settings-managed repository guidance is still present

## Delivery Decision

Release only if:

- the docs match the scripts
- the scripts match the specs
- the fixtures still pass
- the current support boundary is clearly documented
