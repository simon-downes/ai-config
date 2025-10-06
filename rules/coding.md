# General Coding Rules

Core principles and practices for writing maintainable, high-quality code.

## Principles
*Fundamental design principles that guide architectural and structural decisions.*

### SOLID
- **Single Responsibility**: Functions/classes SHOULD have one primary purpose
- **Open/Closed**: You SHOULD extend functionality through new code rather than modifying existing code
- **Liskov Substitution**: Child classes MUST work wherever parent classes are expected
- **Interface Segregation**: You SHOULD create focused interfaces rather than large general ones
- **Dependency Inversion**: You SHOULD depend on interfaces/abstractions when practical

### DRY (Don't Repeat Yourself)
- You SHOULD extract common logic when duplication creates maintenance burden
- You MUST NOT copy-paste code without considering abstraction
- You SHOULD allow minor duplication if it improves code clarity
- You MUST NOT extract code just to reduce line count if it hurts readability

### YAGNI (You Aren't Gonna Need It)
- You MUST implement only explicitly requested features
- You SHOULD NOT add configuration options, parameters or extension points "just in case"
- You MUST resist building generic solutions for specific problems

### KISS (Keep It Simple, Stupid)
- You SHOULD prefer simple, understandable approaches at all levels of design
- You SHOULD avoid unnecessary complexity that doesn't reflect problem complexity
- You SHOULD break complex problems into smaller, simpler parts when it improves overall system clarity
- You SHOULD NOT artificially reduce complexity metrics at the expense of readability or maintainability

## Code Quality
*Standards for writing clear, maintainable, and well-documented code.*

### Documentation
- You MUST add docstrings to all functions and classes
- You MUST include argument and type details in docstrings only if not supported by the language
- You SHOULD add comments when code intent isn't clear from reading
- You MUST keep comments synchronized with code changes

### Type Safety
- You MUST use type hints for all function parameters and return values if the language supports types
- You MUST add variable type annotations if the language supports types
- You MUST utilize type checking and linting tools when available

### Structure
- You MUST use descriptive names (variables, functions, classes) that communicate purpose
- You SHOULD keep functions reasonably small and focused
- You SHOULD group related functionality into modules

## Implementation
*Practical guidelines for building robust, secure, and maintainable functionality.*

### Error Handling
- You SHOULD handle the expected case first, then handle exceptions, rather than checking for every possible failure
- You MUST handle expected and unexpected errors appropriately
- You MUST provide error messages appropriate to the audience/context

### Logging
- You SHOULD implement logging that aids troubleshooting without overwhelming with routine operations
- You MUST use appropriate log levels based on severity and audience
- You MUST follow existing logging patterns in the project, or establish context-appropriate logging if none exists

### Security
- You MUST validate all external inputs
- You MUST NOT hardcode secrets or credentials
- You SHOULD use secure defaults
- You MUST NOT place secrets or credentials in logs unless suitably masked

### General Guidelines
- You SHOULD favor readable and explicit code over compact or abstract code that reduces clarity
- You SHOULD avoid premature optimization but MUST NOT ignore obvious inefficiencies
- You SHOULD prefer composition over inheritance
- You MUST follow consistent formatting and naming patterns
- You SHOULD test important business logic and edge cases
- You MUST separate configuration from code
