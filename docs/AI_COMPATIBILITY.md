# AI Compatibility

This document describes how the USDK Android AI Integration Toolkit maps to common AI coding agents.

## Support Levels

### Native Target

- `Codex` or another Skill-style environment with:
  - local file access
  - local command execution
  - multi-file code editing

This toolkit is authored in that model. The current `SKILL.md`, structured specs, and Python scripts are designed for this environment first.

### High-Confidence Adapters

- `Cline`
- `GitHub Copilot CLI`

These tools are close to the current toolkit shape because they support local commands, file-aware workflows, and configurable agent behavior. They still require packaging or prompt adaptation, but the migration cost is relatively low.

### Secondary Adapters

- `Cursor`
- `Claude Code`

These tools can use the structured specs, templates, and scripts, but they do not natively consume the current `SKILL.md` format. They require a separate adapter layer such as:

- rule files
- agent instructions
- slash command wrappers
- MCP wrapping

### Not Recommended As-Is

- browser-only chat tools
- generic LLM chat surfaces without project access
- tools that cannot read files or run the bundled validation scripts

These environments can read the documentation, but they cannot reliably complete the engineering loop.

## What Must Exist For A Good Integration Experience

Any target AI environment must support:

- reading project files
- running `scripts/usdk_doctor.py`
- optionally running `scripts/usdk_repair_runner.py`
- editing Android project files
- preserving existing project logic while applying template-guided changes

## Current Recommendation Order

1. `Codex`
2. `Cline`
3. `GitHub Copilot CLI`
4. `Cursor`
5. `Claude Code`

## Migration Notes

- `Codex`:
  - use the toolkit directly

- `Cline`:
  - adapt the skill into Cline rules or workflows
  - keep the Python scripts unchanged

- `GitHub Copilot CLI`:
  - adapt the skill into custom instructions, hooks, or agent wrappers
  - keep the Python scripts unchanged

- `Cursor`:
  - rewrite the skill into Cursor rules or `AGENTS.md`
  - preserve the spec and scripts as the execution backend

- `Claude Code`:
  - rewrite the skill into slash commands, local instructions, or subagent workflows
  - preserve the spec and scripts as the execution backend

## Current Boundary

This compatibility note applies to the current toolkit release only. It does not claim turnkey support for every AI listed above. It describes the expected adaptation cost and preferred rollout order.
