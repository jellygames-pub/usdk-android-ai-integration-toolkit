# USDK Android AI Integration Toolkit

Provider-side toolkit for AI-guided USDK Android engineering integration.

Chinese documentation:
- [README.zh-CN.md](README.zh-CN.md)
- [docs/INTEGRATOR_QUICKSTART.zh-CN.md](docs/INTEGRATOR_QUICKSTART.zh-CN.md)
- [docs/CODEX_INTEGRATOR_QUICKSTART.zh-CN.md](docs/CODEX_INTEGRATOR_QUICKSTART.zh-CN.md)
- [docs/USDK_PROVIDER_WORKFLOW.zh-CN.md](docs/USDK_PROVIDER_WORKFLOW.zh-CN.md)
- [docs/GITHUB_RELEASE_v0.2.1.zh-CN.md](docs/GITHUB_RELEASE_v0.2.1.zh-CN.md)
- [docs/INTEGRATOR_INTAKE_TEMPLATE.zh-CN.md](docs/INTEGRATOR_INTAKE_TEMPLATE.zh-CN.md)
- [docs/INTEGRATOR_FAQ.zh-CN.md](docs/INTEGRATOR_FAQ.zh-CN.md)
- `.github/ISSUE_TEMPLATE/integration-support-request.yml`
- `.github/ISSUE_TEMPLATE/bug-report.yml`

Current internal beta note:
- Running the toolkit scripts currently requires Python 3.x on the operator machine.
- This is acceptable for internal testing.
- A no-Python distribution format is not part of `0.2.0`.

## What This Repository Contains

- A Codex skill for USDK Android integration
- A structured integration spec
- A structured repair playbook
- A static doctor script for integration diagnosis
- A repair runner that turns diagnosis into a phased repair plan
- Reusable Java and Gradle template references
- Fixtures and example outputs for validation

## Start Here

- Provider workflow: [docs/USDK_PROVIDER_WORKFLOW.md](docs/USDK_PROVIDER_WORKFLOW.md)
- Integrator quickstart: [docs/INTEGRATOR_QUICKSTART.md](docs/INTEGRATOR_QUICKSTART.md)
- Delivery readiness: [docs/DELIVERY_READINESS.md](docs/DELIVERY_READINESS.md)
- AI compatibility: [docs/AI_COMPATIBILITY.md](docs/AI_COMPATIBILITY.md)
- Provider release checklist: [docs/PROVIDER_RELEASE_CHECKLIST.md](docs/PROVIDER_RELEASE_CHECKLIST.md)
- Skill entry: [skill/usdk-android-integration/SKILL.md](skill/usdk-android-integration/SKILL.md)

## Core Commands

Run diagnosis:

```bash
python scripts/usdk_doctor.py --project-root <android_project_root> --pretty
```

Generate a phased repair plan:

```bash
python scripts/usdk_repair_runner.py --project-root <android_project_root> --format markdown
```

## Current Scope

This release is focused on static Android engineering integration:

- SDK resources and config presence
- Manifest and Gradle wiring
- Application and splash integration
- Consent-gated init flow
- Login, role upload, payment, kick/offline, logout, and exit hooks
- Activity lifecycle forwarding

## Supported AI Environments

- Native target:
  - Codex or another Skill-style environment that can read local files, run local commands, and edit Android projects directly
- High-confidence adapters:
  - Cline
  - GitHub Copilot CLI
- Secondary adapters:
  - Cursor
  - Claude Code

See [docs/AI_COMPATIBILITY.md](docs/AI_COMPATIBILITY.md) for the support model and migration notes.

It does not yet automate:

- Provider console operations
- Backend callback provisioning
- Runtime validation against live SDK binaries
- Optional extension-module integration beyond the core path

## Required Human Confirmations

Some integration decisions are intentionally not guessed by AI and must be explicitly confirmed by the integrator:

- Protocol mode choice:
  - `USDK protocol popup`
  - `Game-owned protocol popup`
- Exit logic reminder:
  - review whether the channel provides its own exit dialog
  - review whether the game must show its own exit confirmation when the channel does not
  - review which user actions should route through the shared exit path

## Delivery Scope

This toolkit is ready for provider-side internal beta and limited pilot use with real Android projects.
It is not yet packaged as a no-Python public installer and it does not automate provider console operations or backend provisioning.

## Release Metadata

- Version: see [VERSION](VERSION)
- Changelog: see [CHANGELOG.md](CHANGELOG.md)
- Toolkit manifest: see [toolkit-manifest.json](toolkit-manifest.json)
