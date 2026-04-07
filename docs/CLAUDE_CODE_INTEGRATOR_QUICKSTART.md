# Claude Code Integrator Quickstart

This guide explains how to use the USDK Android AI Integration Toolkit with Claude Code.

## Official Claude Code Features This Adapter Uses

Claude Code officially supports:

- project memory in `CLAUDE.md`
- project custom slash commands in `.claude/commands/`

This toolkit provides both so the integration workflow is available as shared project context plus reusable commands.

## Recommended Layout

Vendor the toolkit into the target Android project at this path:

```text
<game-project>/
  tools/usdk-android-ai-integration-toolkit/
```

Then copy these adapter files from the toolkit into the target project:

- `adapters/claude/CLAUDE.md` -> `CLAUDE.md`
- `adapters/claude/.claude/commands/usdk-diagnose.md` -> `.claude/commands/usdk-diagnose.md`
- `adapters/claude/.claude/commands/usdk-plan.md` -> `.claude/commands/usdk-plan.md`
- `adapters/claude/.claude/commands/usdk-integrate.md` -> `.claude/commands/usdk-integrate.md`

If the toolkit is vendored somewhere else, update the copied paths before use.

## First Session Checklist

1. Open a terminal in the target Android project.
2. Confirm the project contains the vendored toolkit directory.
3. Start Claude Code in that project root.
4. Run `/usdk-diagnose`.
5. If needed, run `/usdk-plan`.
6. Confirm protocol mode and other required human decisions.
7. Run `/usdk-integrate`.
8. Review the final doctor result and remaining manual inputs.

## Suggested Commands

- `/usdk-diagnose`
- `/usdk-plan`
- `/usdk-integrate`

You can also give plain-language requests after the command if you want to narrow the task.

## Human Decisions Claude Must Not Guess

- protocol mode
- exit-path product logic
- provider console values
- backend callback values
- real role and order field mappings

## Notes

- `CLAUDE.md` is the shared project memory for this integration workflow.
- The bundled commands are plain project commands; teams can edit them as needed.
- The doctor and repair-runner scripts still require Python 3.x on the operator machine in the current toolkit release.
