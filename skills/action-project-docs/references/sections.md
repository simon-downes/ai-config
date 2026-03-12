# Section Guidelines

Detailed guidance on what to include in each documentation section.

---

## README.md Sections

### Project Name and Description

**Purpose:** Immediate understanding of what the project is

**Content:**
- Project name as H1
- 1-2 sentence description
- Primary use case or value proposition

**Example:**
```markdown
# terraform-aws-vpc

Production-ready AWS VPC module with sensible defaults and full customization options.
```

---

### Key Rules

**Purpose:** Quick reference for critical information

**Content:**
- 5-10 imperative statements
- Non-obvious or frequently missed points
- Useful for both humans and agents
- Prioritize safety and correctness

**What to include:**
- Critical constraints
- Common mistakes to avoid
- Required workflows
- Safety requirements

**What to exclude:**
- Obvious information
- Detailed explanations (save for other sections)
- Generic best practices

**Example:**
```markdown
## Key Rules

- Run `make validate` before committing
- Database migrations must be reversible
- All API changes require documentation updates
- Tests must pass in CI before merging
- Never commit `.env` files
```

---

### Installation

**Purpose:** Get the project running

**Content:**
- Prerequisites (runtime, tools, services)
- Step-by-step setup instructions
- Verification steps
- Common setup issues

**Adapt to paradigm:**
- Web app: Include database setup, environment config
- CLI: Package manager install + from-source option
- Library: Package manager install, version requirements
- Collection: Workspace setup, package selection

---

### Usage

**Purpose:** Show how to use the project

**Content:**
- Basic usage examples
- Common workflows
- Key features demonstration
- Links to detailed docs

**Adapt to paradigm:**
- Web app: How to access, key endpoints, authentication
- CLI: Command syntax, common commands, examples
- Library: Import statements, basic API usage, common patterns
- Collection: Which package to use when, cross-package usage

---

### Development

**Purpose:** Brief pointer to contributor information

**Content:**
- One-line summary of dev setup
- Link to CONTRIBUTING.md
- Quick start for contributors

**Example:**
```markdown
## Development

See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup and guidelines.

Quick start:
```bash
make setup
make test
```
```

---

## CONTRIBUTING.md Sections

### Key Rules

**Purpose:** Critical information for contributors

**Content:**
- 5-10 imperative statements
- Focus on contribution-specific rules
- Testing requirements
- Review process essentials

**Example:**
```markdown
## Key Rules

- Create feature branches from `main`
- Write tests for all new features
- Run `make lint` before pushing
- Keep PRs focused and small
- Update documentation with code changes
```

---

### Development Setup

**Purpose:** Get contributors ready to work

**Content:**
- Prerequisites
- Setup commands
- Verification steps
- Troubleshooting common issues

**Be specific:**
- Exact commands to run
- Expected output
- How to verify success

---

### Project Conventions

**Purpose:** Document actual project patterns

**Content:**
- Code organization (why files are where they are)
- Naming conventions (actual patterns used)
- Architecture patterns (how things are structured)
- Configuration approach

**Extract from codebase:**
- Don't prescribe generic standards
- Document what actually exists
- Explain non-obvious choices

**Example:**
```markdown
## Project Conventions

### Directory Structure

- `handlers/` - HTTP request handlers, one file per resource
- `services/` - Business logic, no HTTP concerns
- `models/` - Database models and schemas
- `migrations/` - Database migrations in timestamp order

### Naming

- Handlers: `[resource]_handler.py` (e.g., `user_handler.py`)
- Services: `[domain]_service.py` (e.g., `auth_service.py`)
- Tests: `test_[module].py` matching source structure
```

---

### Testing

**Purpose:** How to run and write tests

**Content:**
- Test commands
- Test organization
- Coverage expectations
- Testing patterns specific to this project

**Be concrete:**
- Actual commands used
- Where tests live
- How to run subsets
- Project-specific test utilities

---

### Contribution Process

**Purpose:** How to submit changes

**Content:**
- Branch naming
- Commit message format
- PR process
- Review expectations
- Merge requirements

**Keep focused:**
- Project-specific process
- Link to external standards (don't duplicate)
- Actual workflow used

---

## AGENTS.md Sections

### Context

**Purpose:** Brief project context for agents

**Content:**
- 1-2 sentences about the project
- Why agent-specific guidance exists

---

### Rules

**Purpose:** Non-obvious constraints for automation

**Content:**
- Safety constraints
- Required human approval points
- Automation boundaries
- State management rules

**Only include:**
- Things that aren't obvious from code
- Project-specific constraints
- Safety-critical information

---

### Hints

**Purpose:** Help agents work effectively

**Content:**
- Project structure insights
- Common patterns
- Useful commands
- Testing considerations

**Focus on:**
- Time-saving information
- Non-obvious relationships
- Effective automation approaches

---

## Distribution Guidelines

### README vs CONTRIBUTING

**README gets:**
- User-facing information
- How to use the project
- Getting started quickly
- High-level overview

**CONTRIBUTING gets:**
- Developer-facing information
- How to modify the project
- Development workflow
- Detailed conventions

**When in doubt:**
- If a user needs it → README
- If only contributors need it → CONTRIBUTING

---

### README/CONTRIBUTING vs AGENTS

**README/CONTRIBUTING get:**
- Information useful to humans
- Detailed explanations
- Examples and tutorials

**AGENTS gets:**
- Non-obvious automation rules
- Safety constraints
- Hints that aren't in code

**When in doubt:**
- If it's obvious from code → Don't include in AGENTS
- If humans need it → README or CONTRIBUTING
- If it's agent-specific safety/efficiency → AGENTS

---

## Anti-Patterns

### Don't Include

**Generic advice:**
```markdown
❌ Follow Python PEP 8 style guide
✅ Use Black formatter with line length 100 (configured in pyproject.toml)
```

**Obvious information:**
```markdown
❌ Write good code
✅ Keep handlers under 100 lines; extract complex logic to services
```

**Duplicated content:**
```markdown
❌ Repeat testing commands in both README and CONTRIBUTING
✅ Brief mention in README, details in CONTRIBUTING
```

**External standards:**
```markdown
❌ Copy entire Git commit message guide
✅ Link to conventional commits, note project-specific requirements
```

---

## Content Principles

1. **Document what exists** - Extract patterns from actual code
2. **Be specific** - Concrete examples over abstract advice
3. **Avoid duplication** - Each fact appears once
4. **Link, don't copy** - Reference external docs
5. **Focus on non-obvious** - Skip what's clear from code
6. **Keep it current** - Documentation should match reality
