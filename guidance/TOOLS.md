# Available Tools

## Shell Usage Guidelines

1. Prefer structured output formats (`--json`, `--yaml`, `--porcelain`) and process them with `jq` or `yq`.

2. Compose tools with pipelines (`|`) instead of writing scripts whenever possible.

3. Use shell chaining for control flow:
   - `cmd1 && cmd2` (run on success)
   - `cmd1 || cmd2` (fallback on failure)

4. Use command grouping `{ ...; }` or `( ... )` when multiple commands share the same context.

5. Prefer modern CLI utilities for discovery and filtering:
   - `fd` for file discovery
   - `rg` for searching file contents
   - `jq` / `yq` for structured data processing.

## Standard Tools
**Code:** rg (ripgrep), fd, tree, shellcheck, shfmt
**Data:** jq, yq
**Cloud:** gh, aws, tofu
**Python:** uv, python3

## Enhanced Tools

### difft (Difftastic)
Structural diff that understands code syntax. Use when comparing code files for better readability.

```bash
# Compare two files
difft file1.py file2.py

# Use with git
git diff | difft --color=always

# Compare directories
difft --display side-by-side old/ new/
```

**When to use:** Code reviews, refactoring verification, understanding complex changes.

### xh
HTTP client with better defaults for JSON APIs. Use over curl for quick API testing.

```bash
# GET request (auto-formats JSON)
xh https://api.example.com/users

# POST JSON (auto-detects)
xh POST https://api.example.com/users name=john email=john@example.com

# Headers
xh https://api.example.com/data Authorization:"Bearer token"

# Download file
xh --download https://example.com/file.zip
```

**When to use:** Testing APIs, quick HTTP requests with JSON, debugging endpoints.

## Agent Kit Tools

### ak kv - Key-Value Storage
Simple persistent storage for configuration and state.

```bash
# Set values
ak kv set api-key "sk-..."
ak kv set --namespace config db-host "localhost"

# Get values
ak kv get api-key
ak kv get --namespace config db-host

# List all keys
ak kv list
ak kv list --namespace config

# Delete
ak kv delete api-key
```

**Use for:** API keys, configuration values, temporary state between commands.

### ak log - Activity Log
Capture and retrieve project activity. Auto-detects project from cwd.

```bash
# Add entry (project auto-detected)
ak log add --kind decision "chose uv over pip for dependency management"
ak log add --kind change "migrated auth module to OAuth2" --topic auth

# Explicit project
ak log add --kind change "fixed auth bug" --project my-app

# List entries (project optional for cross-project queries)
ak log list
ak log list --kind decision --limit 5
ak log list --since 7d
ak log list --since 2026-03-01 --until 2026-03-15

# View statistics
ak log stats
ak log stats --project my-app
```

**Kinds:** task, decision, change, issue, note, request
**Use for:** Tracking decisions, capturing activity, noting issues, recording requests.

### ak project
Show project name for a directory (used by mem for auto-detection).

```bash
# Current directory
ak project

# Specific path
ak project /path/to/project
```

**Resolution:** First subdirectory under ~/dev, then git root, then path-based.

### ak check
Verify tool installation and authentication status.

```bash
# Check all configured tools
ak check

# Check specific tools
ak check gh aws

# Verbose output with auth details
ak check -v
```

**Config:** `~/.agent-kit/tools.yaml` - defines tools, version commands, auth checks.

### ak oauth
Manage OAuth tokens for services.

```bash
# Store token
ak oauth set github "ghp_..."
ak oauth set --service notion "secret_..."

# Retrieve token
ak oauth get github

# List services
ak oauth list

# Delete token
ak oauth delete github
```

**Use for:** Storing OAuth tokens securely, managing API credentials.

### ak notion
Interact with Notion API.

```bash
# Query database
ak notion query-database <database-id>

# Get page
ak notion get-page <page-id>

# Create page
ak notion create-page <parent-id> --title "Page Title"
```

**Requires:** OAuth token via `ak oauth set notion "secret_..."`

