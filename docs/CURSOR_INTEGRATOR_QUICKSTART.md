# Cursor Integrator Quickstart

This guide explains how to use the USDK Android AI Integration Toolkit with Cursor.

## Official Cursor Features This Adapter Uses

Cursor officially supports:

- `AGENTS.md` in the project root as a simple agent-instruction file
- Project Rules in `.cursor/rules/*.mdc`

This toolkit provides both formats so integrators can choose the simpler or more structured path.

## Recommended Layout

Vendor the toolkit into the target Android project at this path:

```text
<game-project>/
  tools/usdk-android-ai-integration-toolkit/
```

Then copy these adapter files from the toolkit into the target project root:

- `adapters/cursor/AGENTS.md` -> `AGENTS.md`
- `adapters/cursor/.cursor/rules/usdk-android-integration.mdc` -> `.cursor/rules/usdk-android-integration.mdc`

If the toolkit is vendored somewhere else, update the copied paths before use.

## First Session Checklist

1. Open the target Android project in Cursor.
2. Confirm the project contains the vendored toolkit directory.
3. Ask Cursor to diagnose the project before editing.
4. If the diagnosis is non-trivial, ask Cursor to generate a phased repair plan.
5. Confirm protocol mode and other required human decisions.
6. Let Cursor edit the project.
7. Ask Cursor to re-run the doctor and summarize the remaining manual inputs.

## Suggested Prompts

Diagnosis:

```text
Read AGENTS.md and the Cursor rule, then run the USDK doctor for this project and summarize the result.
```

Repair planning:

```text
Use the vendored USDK toolkit to generate a phased repair plan for this Android project.
```

Integration:

```text
Use the vendored USDK toolkit to integrate USDK into this project. Confirm protocol mode before editing, remind me about exit logic, apply the required changes, and re-run the doctor afterward.
```

## Human Decisions Cursor Must Not Guess

- protocol mode
- exit-path product logic
- provider console values
- backend callback values
- real role and order field mappings

## Notes

- Cursor can use either `AGENTS.md` or `.cursor/rules`. Keeping both is fine.
- The doctor and repair-runner scripts still require Python 3.x on the operator machine in the current toolkit release.
