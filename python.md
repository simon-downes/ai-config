# Python Coding Rules

Python-specific standards, idioms, and toolchain requirements for writing quality code.

## Preferred Toolchain
*Standard tools for Python development.*

### Package Management
- You MUST use `uv` for dependency management and virtual environments
- You MUST define dependencies in `pyproject.toml`
- You SHOULD separate development dependencies using `uv add --dev`

### Code Quality
- You MUST use Black for code formatting if no existing code formatting tool is present
- You MUST use Ruff for linting if no existing linter is present
- You SHOULD run ruff and black after making changes.

### Testing
- You MUST use pytest for testing if no existing test framework or library is present
- You SHOULD use pytest fixtures for test setup
- You MUST organize tests in a `tests/` directory
- You SHOULD aim for meaningful test names that describe behavior

### Configuration
- You SHOULD configure tools in `pyproject.toml` when possible
- You MUST ensure Black and Ruff configurations are compatible

## Code Style
*Python-specific standards and idioms.*

### Style and Formatting
- You MUST follow PEP 8 style guidelines
- You MUST use 4 spaces for indentation, never tabs
- You SHOULD limit lines to 88 characters (Black formatter standard)
- You MUST surround top-level functions and classes with two blank lines
- You MUST follow Google-style docstrings
- You SHOULD use blank lines to separate logical sections
- You MUST NOT include trailing whitespace
- You MUST end files with a single newline

### Naming
- Modules: short, lowercase (`users.py`, `db.py`)
- Packages: short, lowercase, no underscores (`mypackage`)
- Classes: PascalCase, nouns (`UserProfile`, `DatabaseConnection`)
- Functions: snake_case, verbs (`get_user`, `connect_to_db`)
- Variables: snake_case, nouns (`user_list`, `connection_pool`)
- Constants: UPPER_SNAKE_CASE (`MAX_CONNECTIONS`, `DEFAULT_TIMEOUT`)
- Protected: single underscore (`_internal_method`)
- Private: double underscore (`__very_private`)


### Language Features

- You MUST use type hints for variables and function signatures
- You SHOULD use idiomatic Python constructs
   - list/dict comprehensions
   - enumerate()
   - with statements and context managers
   - unpacking — instead of verbose or manual equivalents.
   - dict.get() with defaults instead of checking key existence
- You SHOULD use specific exception types, not bare `except:`
- You SHOULD use `*args` and `**kwargs` judiciously, with clear documentation
- You MUST define `__str__` and `__repr__` methods for custom classes
- You MUST group imports: standard library, third-party, local
- You SHOULD use absolute imports over relative imports
- You MUST NOT use wildcard imports (`from module import *`)
- You SHOULD import modules, not individual functions when importing many items
