# Documentation Templates

This file contains template sections for different project paradigms.

Compose documentation by selecting relevant sections based on the project's characteristics.

---

## README.md Templates

### Key Rules Section (All Projects)

```markdown
## Key Rules

- [Most critical rule for users/contributors]
- [Second most important rule]
- [Third most important rule]
- [Additional rules as needed, max ~10]
```

Guidelines:
- Write in imperative mood
- Focus on non-obvious or critical points
- Useful for both humans and AI agents
- Avoid stating the obvious

---

### Web App Sections

#### Installation

```markdown
## Installation

### Prerequisites

- [Runtime/platform requirements]
- [Database requirements]
- [External service dependencies]

### Setup

1. Clone the repository
2. Install dependencies: `[command]`
3. Configure environment variables (see Configuration)
4. Run database migrations: `[command]`
5. Start the server: `[command]`
```

#### Configuration

```markdown
## Configuration

Required environment variables:

- `VAR_NAME` - Description
- `VAR_NAME` - Description

Optional:

- `VAR_NAME` - Description (default: value)
```

#### Usage

```markdown
## Usage

Access the application at `http://localhost:[port]`

### API Endpoints

See [API documentation](link) for complete reference.

Key endpoints:
- `GET /endpoint` - Description
- `POST /endpoint` - Description
```

#### Deployment

```markdown
## Deployment

[Brief deployment instructions or link to deployment docs]

Environment-specific configurations:
- Development: [details]
- Staging: [details]
- Production: [details]
```

---

### CLI Tool Sections

#### Installation

```markdown
## Installation

### From Package Manager

```bash
[package-manager] install [package-name]
```

### From Source

```bash
git clone [repo]
cd [repo]
[build/install command]
```
```

#### Usage

```markdown
## Usage

Basic syntax:

```bash
[tool-name] [command] [options]
```

### Commands

- `[command]` - Description
- `[command]` - Description

### Examples

```bash
# Example 1
[tool-name] [command] [args]

# Example 2
[tool-name] [command] [args]
```
```

#### Configuration

```markdown
## Configuration

Configuration file location: `[path]`

Example configuration:

```[format]
[example config]
```

Environment variables:
- `VAR_NAME` - Description
```

---

### Single Library Sections

#### Installation

```markdown
## Installation

```bash
[package-manager] install [package-name]
```

Requirements:
- [Language/runtime version]
- [Optional dependencies]
```

#### Usage

```markdown
## Usage

```[language]
[import statement]

[basic usage example]
```

### API Overview

- `[function/class]` - Description
- `[function/class]` - Description

See [API documentation](link) for complete reference.
```

#### Compatibility

```markdown
## Compatibility

- [Language] [version range]
- [Platform requirements]
- [Known limitations]
```

---

### Collection of Libraries Sections

#### Repository Structure

```markdown
## Repository Structure

```
[package-1]/     - Description
[package-2]/     - Description
[shared]/        - Description
```

Each package has its own README with detailed usage.
```

#### Getting Started

```markdown
## Getting Started

This repository contains multiple related packages:

- **[package-1]**: Description and use case
- **[package-2]**: Description and use case

### Installation

Install individual packages:

```bash
[package-manager] install [package-name]
```

Or install from source:

```bash
git clone [repo]
cd [repo]
[build command]
```
```

#### Development

```markdown
## Development

### Workspace Setup

```bash
[workspace setup commands]
```

### Working with Multiple Packages

- [Cross-package development workflow]
- [Dependency management approach]
- [Testing across packages]
```

---

## CONTRIBUTING.md Templates

### Key Rules Section (All Projects)

```markdown
## Key Rules

- [Most critical rule for contributors]
- [Second most important rule]
- [Third most important rule]
- [Additional rules as needed, max ~10]
```

---

### Development Setup (All Projects)

```markdown
## Development Setup

### Prerequisites

- [Tool/runtime requirements]
- [Development tool requirements]

### Setup Steps

1. Clone the repository
2. [Setup command 1]
3. [Setup command 2]
4. Verify setup: `[verification command]`
```

---

### Project Conventions (All Projects)

```markdown
## Project Conventions

### Code Organization

- [Directory structure explanation]
- [File naming conventions]
- [Module organization patterns]

### Code Style

This project follows [language] conventions with these specifics:

- [Project-specific style rule]
- [Project-specific style rule]

[Link to linter config or style guide if applicable]

### Naming Conventions

- [Naming pattern 1]
- [Naming pattern 2]
```

---

### Testing (All Projects)

```markdown
## Testing

### Running Tests

```bash
[test command]
```

### Test Organization

- [Test directory structure]
- [Test naming conventions]
- [Test coverage expectations]

### Writing Tests

- [Project-specific testing patterns]
- [Fixture/mock conventions]
- [Integration test approach]
```

---

### Contribution Process (All Projects)

```markdown
## Submitting Changes

1. Create a feature branch: `git checkout -b feature-name`
2. Make your changes
3. Run tests: `[test command]`
4. Commit with clear message
5. Push and create pull request

### Pull Request Guidelines

- [PR description requirements]
- [Review process]
- [Merge requirements]

### Commit Messages

[Commit message format or link to convention]
```

---

### Web App Specific

```markdown
## Database Changes

### Migrations

Create migration:
```bash
[migration command]
```

Apply migrations:
```bash
[apply command]
```

### Seeding Data

[Seeding approach and commands]
```

---

### CLI Tool Specific

```markdown
## Adding Commands

1. [Where to add command code]
2. [Command structure pattern]
3. [Argument parsing approach]
4. [Testing commands]
```

---

### Library Specific

```markdown
## API Design

- [Public API conventions]
- [Backward compatibility policy]
- [Deprecation process]

## Documentation

- [Docstring format]
- [Example requirements]
- [API doc generation]
```

---

## AGENTS.md Templates

AGENTS.md should only be created when there are non-obvious rules or constraints for AI agents.

### Basic Structure

```markdown
# Agent Guidelines

[1-2 sentence project context]

## Rules

- [Non-obvious rule that agents should follow]
- [Safety constraint]
- [Automation boundary]

## Hints

- [Helpful context about project structure]
- [Common pitfalls to avoid]
- [Effective automation approaches]
```

### Examples of Agent-Specific Content

**State management:**
```markdown
## Rules

- Never modify Terraform state files directly
- Always run `terraform plan` before `terraform apply`
- State changes require human approval
```

**Safety constraints:**
```markdown
## Rules

- Database migrations must be reviewed by a human before execution
- Never commit secrets or credentials
- Production deployments require manual approval
```

**Automation hints:**
```markdown
## Hints

- Test fixtures are generated from `scripts/generate-fixtures.py`
- The `make validate` command runs all pre-commit checks
- Integration tests require Docker and take ~5 minutes
```

**Project-specific context:**
```markdown
## Hints

- The `core/` directory contains stable APIs, `experimental/` may change
- Configuration is validated against JSON schema in `schemas/`
- Each module in `modules/` is independently versioned
```
