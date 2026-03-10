# Agent Workspace

Personal AI-assisted coding workflow tooling for Kiro CLI.

## Overview

This workspace provides the configuration, agents, and skills that power my AI-assisted development workflow. It consists of three repositories that work together:

- **agent-workspace** (this repo) - Agent configurations, skills, and installation tooling
- **agent-kit** - CLI utilities for development workflows (key-value storage, OAuth, Notion integration)
- **agent-executor** - Unified execution hub for running AI tools in isolated Docker containers

## Repository Structure

The `agent-kit` and `agent-executor` repositories should be checked out as subdirectories alongside this main repository:

```
agent-workspace/
├── agent-kit/          # git clone https://github.com/simon-downes/agent-kit
├── agent-executor/     # git clone https://github.com/simon-downes/agent-executor
├── agents/             # Custom agent configurations
├── skills/             # Reusable knowledge modules
└── install.sh          # Installation script
```

Both subdirectories are git-ignored to keep the repositories logically separate.

## Components

### Agents

Custom agent configurations with specialized tool access and workflows:
- `principal-engineer` - Sandbox-only agent with unrestricted capabilities
- `principal-engineer-safe` - Production-safe variant with restricted access
- `platform-engineering` - Platform-focused agent for AWS/infrastructure work

### Skills

Progressive-loading knowledge modules that activate based on context:
- Language-specific expertise (Terraform, Python)
- General coding principles and practices
- Tool-specific workflows (Git/GitHub)
- Planning, implementation, and review workflows

### Installation

Run `./install.sh` to deploy agents and skills to `~/.kiro/`.

## Related Projects

- [agent-kit](./agent-kit/README.md) - CLI toolkit for development workflows
- [agent-executor](./agent-executor/README.md) - Sandboxed execution environment for AI tools
