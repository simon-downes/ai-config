---
name: action-project-docs
description: >
  Generate or update README.md, CONTRIBUTING.md, and AGENTS.md files for projects by analyzing codebase structure and applying paradigm-appropriate templates. Use this skill when creating project documentation from scratch, updating existing documentation files, refactoring documentation structure, adding missing documentation files, improving documentation to follow best practices, or when the user requests to "update project docs" or "create a README/CONTRIBUTING/AGENTS file".
---

# Purpose

Generate and maintain high-quality project documentation (README.md, CONTRIBUTING.md, AGENTS.md) that is:

- Accurate to the actual codebase
- Appropriate for the project paradigm
- Minimal and focused
- Free from duplication
- Useful for both humans and AI agents

---

# When to Use

Use this skill when:

- Creating documentation for a new project
- Updating existing documentation after significant changes
- Refactoring documentation structure
- Adding missing documentation files
- Improving documentation to follow best practices

---

# When Not to Use

Do not use this skill for:

- Minor typo fixes or small edits (handle directly)
- API documentation or code comments (different concern)
- Detailed architecture docs (should be separate files)
- Release notes or changelogs (different format)

---

# Workflow

## 1. Determine scope

Check which files exist and what the user wants:

- Does README.md exist?
- Does CONTRIBUTING.md exist?
- Does AGENTS.md exist?
- Is this creation, update, or improvement?

Default to treating README + CONTRIBUTING as a unified set. Only create AGENTS.md if there are non-obvious agent-specific concerns.

---

## 2. Analyze the codebase

Examine the project to understand:

**Project paradigms** (can be multiple):
- Web app: HTTP service, API, web interface
- CLI tool: Command-line interface
- Single library/module: One cohesive package
- Collection of libraries/modules: Multiple related packages

**Technical details:**
- Primary languages
- Frameworks and key dependencies
- Build/test tooling
- Package structure
- Entry points
- Configuration approach
- Deployment artifacts (if any)

**Existing patterns:**
- Code organization conventions
- Testing approach
- Documentation style
- Contribution history (if git repo)

Read existing documentation files if present to understand current state.

---

## 3. Identify information gaps

Determine what information is:
- Available from codebase analysis
- Missing or ambiguous
- Needs user clarification

Prepare questions for the user about missing details.

---

## 4. Select template sections

Based on identified paradigms, select relevant sections from templates (see `references/templates.md`).

Projects can match multiple paradigms - compose documentation from all applicable sections.

Common sections by paradigm:

**Web app:**
- API endpoints or UI access
- Environment variables
- Database setup
- Deployment instructions

**CLI tool:**
- Installation methods
- Command examples
- Configuration options
- Common workflows

**Single library:**
- Installation from package manager
- Import/usage examples
- API reference link
- Version compatibility

**Collection:**
- Repository structure
- Package purposes
- Cross-package dependencies
- Development workflow

---

## 5. Draft documentation structure

Create an outline showing:
- Which sections will appear in each file
- How information is distributed to avoid duplication
- What "Key Rules" will be highlighted

Show this structure to the user before generating content.

---

## 6. Generate content

For each file:

**README.md:**
- Key Rules section (imperative, agent-friendly)
- Project overview
- Getting started / installation
- Usage examples
- Development setup (brief, link to CONTRIBUTING)
- Links to detailed docs

**CONTRIBUTING.md:**
- Key Rules section (imperative, agent-friendly)
- Development environment setup
- Project-specific conventions and patterns
- Testing approach
- PR/contribution process
- Links to external standards (don't duplicate)

**AGENTS.md (optional):**
- Non-obvious rules for AI agents
- Safety constraints
- Project-specific automation hints
- Areas requiring human review

**Content principles:**
- Document what exists, not preferences
- Extract actual patterns from the codebase
- Be specific and concrete
- Avoid generic advice
- Link to detailed docs rather than duplicating
- Keep "Key Rules" to 5-10 critical points

---

## 7. Deduplicate across files

Review all generated content and ensure:
- Each piece of information appears once
- Information is in the most appropriate file
- Files reference each other when needed

**Distribution guidelines:**
- README: User-facing, getting started
- CONTRIBUTING: Developer-facing, how to work on the project
- AGENTS: AI-specific, non-obvious automation concerns

---

## 8. Prompt for missing information

Ask the user targeted questions about:
- Ambiguous details
- Missing context
- Choices between alternatives

Ask one question at a time. Provide options when helpful.

---

## 9. Present for approval

Show the complete content of all files to be created or updated.

For updates, highlight what's changing from existing files.

Wait for explicit approval before writing files.

---

## 10. Write files

After approval:
- Write README.md
- Write CONTRIBUTING.md
- Write AGENTS.md (if applicable)
- Report what was created/updated

---

# Output Format

Each documentation file should follow this structure:

## README.md

```markdown
# Project Name

Brief description (1-2 sentences)

## Key Rules

- Rule 1
- Rule 2
- Rule 3

## [Paradigm-specific sections]

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md)
```

## CONTRIBUTING.md

```markdown
# Contributing

## Key Rules

- Rule 1
- Rule 2
- Rule 3

## Development Setup

## Project Conventions

## Testing

## Submitting Changes
```

## AGENTS.md (if needed)

```markdown
# Agent Guidelines

Brief context about the project.

## Rules

- Non-obvious rule 1
- Non-obvious rule 2

## Safety Constraints

- Constraint 1

## Hints

- Helpful hint 1
```

---

# Examples

## Example 1: New Python CLI tool

**User request:**
"Create documentation for this project"

**Analysis:**
- Single Python package with Click CLI
- Entry point in `__main__.py`
- Uses pytest for testing
- No existing docs

**Output:**
README.md with installation, command examples, development setup
CONTRIBUTING.md with Python conventions, testing approach, PR process
No AGENTS.md (no special agent concerns)

---

## Example 2: Update docs for web app

**User request:**
"Update the README, we added authentication"

**Analysis:**
- Existing README and CONTRIBUTING
- New auth middleware and environment variables
- Database migrations added

**Output:**
Updated README.md with new environment variables and auth setup
Updated CONTRIBUTING.md with migration workflow
Preserved existing structure and style

---

## Example 3: Terraform module collection

**User request:**
"Generate project docs"

**Analysis:**
- Multiple Terraform modules in subdirectories
- Each module has examples/
- Shared variables pattern
- No existing docs

**Output:**
README.md with module overview, usage examples, module listing
CONTRIBUTING.md with Terraform conventions, testing with terratest, module structure
AGENTS.md with rules about state management and variable validation
