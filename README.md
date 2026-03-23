# Agent Workspace

Personal AI-assisted coding workflow tooling for Kiro CLI.

## Overview

This workspace provides the configuration, agents, and skills that power my AI-assisted development workflow. It consists of three repositories that work together:

- **agent-workspace** (this repo) - Agent configurations, skills, prompts, and installation tooling
- **agent-kit** - CLI utilities for development workflows (`ak` command — key-value storage, activity logging, OAuth, Notion)
- **agent-executor** - Unified execution hub for running AI tools in isolated Docker containers

## Repository Structure

```
agent-workspace/
├── agents/             # Agent configurations (JSON)
├── skills/             # Layered knowledge modules (SKILL.md + references)
├── prompts/            # System prompts for agents
├── guidance/           # Steering files (installed to ~/.kiro/steering/)
├── agent-kit/          # git subdir — CLI toolkit
├── agent-executor/     # git subdir — sandboxed execution
└── install.sh          # Deploy to ~/.kiro/
```

`agent-kit` and `agent-executor` are separate git repositories checked out as subdirectories (git-ignored).

## Agents

Two orchestrator agents with different permission levels, plus five read-only subagents:

**Orchestrators:**
- `principal-engineer-safe` — restricted writes, requires approval for destructive commands
- `principal-engineer-sandbox` — unrestricted, for use in sandboxed environments

**Subagents** (read-only, spawned by orchestrators):
- `general-purpose` — research, investigation, ad-hoc tasks
- `code-reviewer` — code quality review
- `plan-reviewer` — plan completeness review
- `qa-runner` — formatting, linting, tests
- `codebase-analyzer` — deep codebase analysis

Orchestrators own all file mutations. Subagents gather information and return findings.

## Skills

Skills are layered knowledge modules that activate based on context and user intent.

| Layer | Skills | Purpose |
|-------|--------|---------|
| **Policy** | `policy-general-coding`, `policy-lang-python`, `policy-lang-terraform` | Standards and conventions |
| **Workflow** | `workflow-plan`, `workflow-implement`, `workflow-review` | Core orchestration (plan → implement → review) |
| **Tool** | `tool-git-github` | Operational guidance for CLI tools |
| **Action** | `action-create-skill`, `action-project-docs`, `action-analyze-codebase`, `action-review-plan`, `action-create-terraform-module` | Self-contained tasks |

See `skills/action-create-skill/references/LAYERS.md` for layer definitions.

## Installation

```bash
./install.sh
```

Copies agents, skills, prompts, and guidance to `~/.kiro/`. The workspace files are the source of truth; `~/.kiro/` is the install target.

## Related Projects

- [agent-kit](./agent-kit/README.md) — CLI toolkit for development workflows
- [agent-executor](./agent-executor/README.md) — Sandboxed execution environment for AI tools
