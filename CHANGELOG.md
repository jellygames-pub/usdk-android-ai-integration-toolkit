# Changelog

## 0.2.1

- Added Chinese delivery documentation for provider workflow, integrator quickstart, delivery readiness, AI compatibility, and release checklist
- Added a Chinese Codex-specific quickstart for integrators using this toolkit with local projects
- Updated the repository README to link the new Chinese documentation set

## 0.2.0

- Expanded the runtime coverage to include explicit role-reporting hooks for `enterGame`, `createNewRole`, and `roleLevelUp`
- Added required `setKickListener` coverage to the sample project, doctor checks, playbook, and templates
- Refined the protocol flow so integrators must explicitly choose between the USDK popup path and the game-owned popup path
- Refined the exit flow so the sample and templates check `isChannelHasExitDialog()` before deciding whether the game must show its own local exit confirmation
- Added a strong exit-logic reminder to the skill and delivery docs without turning exit logic into a separate branch choice
- Expanded the sample `RoleInfo` and `OrderInfo` builders into fuller field-mapping skeletons for real project handoff
- Added delivery-facing documentation for supported AI environments, delivery readiness, and provider release checks

## 0.1.1

- Added Gradle 7+ and settings-managed repository guidance for local USDK `flatDir` resolution
- Updated doctor logic to recognize settings-level `flatDir` repositories
- Updated Gradle templates to separate Gradle 7+ repository placement from older project-managed setups
- Completed a real sample-project static integration trial and documented the result
- Added clearer Python 3.x internal-beta runtime notes in the toolkit docs

## 0.1.0

Initial provider toolkit release.

- Added the USDK Android integration skill
- Added the structured integration spec
- Added the structured repair playbook
- Added the static doctor script
- Added the phased repair runner
- Added template references for application, splash, runtime chain, lifecycle, and Gradle variants
- Added native and partial Android fixtures
- Added before and after example reports and repair plans
