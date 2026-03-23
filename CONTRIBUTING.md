# Contributing

## Project Layout

- `agents/` — JSON configs defining tool access, allowed commands, and resources per agent
- `skills/` — each skill is a directory with `SKILL.md` and optional `references/`, `scripts/`, `assets/`
- `prompts/` — system prompts (`.prompt.md`) for agents that need behavioural instructions
- `guidance/` — steering files installed to `~/.kiro/steering/` (tool guidance, shell conventions)
- `install.sh` — deploys everything to `~/.kiro/`

## Conventions

**Skills** follow a layered naming convention (`policy-*`, `workflow-*`, `tool-*`, `action-*`). See `skills/action-create-skill/references/LAYERS.md` for definitions. Use the `action-create-skill` skill when creating or modifying skills.

**Agent configs** pair with prompts by name: `agents/foo.json` uses `prompts/foo.prompt.md`. Not all agents need prompts (e.g., `general-purpose` has no prompt file).

**Orchestrator/subagent split:** orchestrator agents (`principal-engineer-*`) own all file writes. Subagents are read-only and return findings to the orchestrator.

**RFC 2119 keywords** (MUST/SHOULD/MAY) are used in policy skills to distinguish hard rules from recommendations.

## Making Changes

1. Edit files in this workspace (source of truth)
2. Run `./install.sh` to deploy to `~/.kiro/`
3. Test in a Kiro CLI session

**Skill changes:** verify activation phrases still trigger correctly and don't collide with other skills.

**Agent config changes:** ensure `allowedCommands` and `trustedAgents` are consistent across related agents.

## Dependencies

- [Kiro CLI](https://kiro.dev) — the AI assistant that consumes these configs
- [agent-kit](./agent-kit/README.md) — provides the `ak` command used by skills for logging, key-value storage, etc.
