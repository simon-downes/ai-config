# AI Config

Personal AI tooling configuration for Kiro CLI, optimized for platform engineering workflows.

## Overview

This repository contains custom agent configurations and skills for use with Kiro CLI, providing:
- Specialized agent personas with tailored tool access and workflows
- Progressive-loading skills for language-specific and general coding standards
- Installation tooling for easy deployment

## Structure

- **agents/** - Custom agent configurations
  - `principal-engineer` - Primary agent for sandbox use with broad capabilities
  - `principal-engineer-safe` - Production-safe variant with restricted access
  - `platform-engineering` - Platform-focused agent with AWS/Terraform expertise
- **skills/** - Reusable knowledge modules
  - `lang-terraform-expertise` - Terraform/OpenTofu coding standards
  - `lang-python-expertise` - Python coding standards with modern tooling
  - `general-coding-expertise` - Language-agnostic principles and practices
  - `tool-git-github` - Git and GitHub workflows
- **sandbox/** - Docker-based sandbox environment for Kiro CLI
- **install.sh** - Installation script to deploy agents and skills to ~/.kiro/

## Installation

Run the installation script to copy agents and skills to your Kiro configuration:

```bash
./install.sh
```

This copies:
- Agents to `~/.kiro/agents/`
- Skills to `~/.kiro/skills/`

## Agents

### principal-engineer

Sandbox-only agent with unrestricted tool access, designed for isolated execution. Features iteration-based workflow, progressive enhancement, and broad capabilities (file ops, shell, AWS, web, code intelligence). Keyboard shortcut: `ctrl+p`

**⚠️ Only use in sandbox - unrestricted permissions make it unsafe for direct use.**

### principal-engineer-safe

Production-safe variant of principal-engineer with restricted file and command access. Safe for local use with controlled permissions (specific file extensions, read-only AWS operations, safe shell commands). Keyboard shortcut: `ctrl+p`

### platform-engineering

Platform-focused agent for AWS/infrastructure work with restricted tool access.

## Skills

Skills use progressive disclosure - metadata loads at startup, full content loads on-demand when relevant.

### lang-terraform-expertise
Terraform/OpenTofu coding standards including file organization, naming conventions, resource patterns, and tagging.

### lang-python-expertise
Python coding standards with modern tooling (uv, Black, Ruff, pytest), type hints, and idiomatic patterns.

### general-coding-expertise
Language-agnostic principles (SOLID, DRY, YAGNI, KISS) and practices for maintainable code.

### tool-git-github
Git and GitHub workflows including branch naming, commit standards, PR operations, code review, and cross-repo queries.

## Sandbox

Docker-based sandbox environment for Kiro CLI with:
- Isolated filesystem access
- Pre-configured with principal-engineer agent
- Essential platform engineering tools (OpenTofu, AWS CLI, etc.)
- Automatic conversation resumption

See [sandbox/README.md](sandbox/README.md) for details.

## Usage

After installation, agents and skills are available globally:

```bash
# Use principal-engineer-safe agent (local, production-safe)
kiro-cli chat --agent principal-engineer-safe

# Use platform-engineering agent
kiro-cli chat --agent platform-engineering

# Use principal-engineer agent (via sandbox only)
cd sandbox
./kiro
```

Skills activate automatically based on context (e.g., working with .tf or .py files).
