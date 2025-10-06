# Rule Fetcher

A script to collect context and rules for AI agents from various sources into a single directory,
that can then be included in agent config for automatic loading.

It can also be used for the more general task of aggregating documentation from different sources.

It was build specifically to handle the fact that Amazon Q has no concept of global rules, but an engineering team
would likely have rules and context that would span multiple projects and duplicating everything would be very bad.

## Usage

### Configuration File

Create a YAML configuration file (default `~/.agent-rules.yaml`) specifying sources and output directory:

```yaml
sources:
  - ../rules/coding.md             # Local file (relative or absolute path)
  - /path/to/directory             # Directory (finds *.md files)
  - /path/to/files/*.md            # Glob pattern
  - https://example.com/file.md    # Web URL
output: /tmp/my-rules              # Output directory (must exist)
```

### Running

**Directly from GitHub (Recommended):**
```bash
uvx --from git+https://github.com/simon-downes/ai-rules.git#subdirectory=rule-fetcher fetch-rules config.yaml
```

**Locally:**
```bash
uv run fetch-rules.py my-config.yaml
```
> [!NOTE]
> Config file argument is optional and will use the default if not provided.

## Restricted Sources

The tool includes built-in safety checks to prevent dangerous operations:

- **Dangerous directories blocked**: `/`, `/proc`, `/sys`, `/dev`, `/run`, `/root`
- **Dangerous glob patterns blocked**: `/`, `/*`, `/**`
- **File limits**: Directory and glob searches limited to 25 files

## Project Structure

```
rule-fetcher/
├── fetch_rules.py          # Main script
├── agent-rules.yaml        # Example configuration
├── pyproject.toml          # Project configuration
├── tests/
│   ├── test_fetch_files.py # Test suite
│   └── test-output/        # Test output directory
└── README.md               # This file
```

## Contributing

### Development Setup

```bash
# Install development dependencies
uv sync --dev
```

### Tooling

- **Black** for code formatting
- **Ruff** for linting
- **pytest** for testing

```bash
# Format code
uv run black fetch_rules.py

# Lint code
uv run ruff check fetch_rules.py

# Run tests
uv run pytest tests/ -v
```
