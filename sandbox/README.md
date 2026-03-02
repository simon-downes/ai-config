# Kiro CLI Sandbox

A Docker-based sandbox environment for running [Kiro CLI](https://kiro.dev) with isolated filesystem access and enhanced tooling for platform engineering workflows.

## Overview

This sandbox provides a containerized environment for Kiro CLI that:
- Isolates filesystem changes to specific working directories
- Shares credentials and conversation history with your host system
- Includes essential platform engineering tools (AWS CLI, OpenTofu, jq, yq, etc.)
- Supports multiple concurrent sessions across different directories
- Provides automatic conversation resumption

## Requirements

- macOS (tested on Apple Silicon and Intel)
- [Docker Desktop](https://www.docker.com/products/docker-desktop) or [Colima](https://github.com/abiosoft/colima)
- Kiro CLI account (sign up at [kiro.dev](https://kiro.dev))
- Working directory must be under your home directory

## Getting Started

### Initial Setup

1. Clone or download this repository
2. Navigate to the sandbox directory
3. Make the wrapper script executable:
   ```bash
   chmod +x kiro
   ```

### First Run

On first run, the sandbox will automatically:
1. Build the Docker image (this takes a few minutes)
2. Prompt you to authenticate with Kiro CLI using device flow
3. Start an interactive chat session

```bash
./kiro
```

### Basic Usage

```bash
# Start Kiro CLI in current directory
./kiro

# Start Kiro CLI in a specific directory
./kiro /path/to/project

# Pass commands directly to Kiro CLI
./kiro chat
./kiro doctor

# Open a bash shell in the sandbox
./kiro --shell

# Rebuild the Docker image
./kiro --rebuild

# List running sessions
./kiro --list

# Stop a specific session
./kiro --stop dev-ai-config

# Show help
./kiro --help
```

## Features

### Session Management

Each directory gets its own isolated session:
- Session names are automatically generated from directory paths
- Only one session per directory can run at a time
- Multiple sessions can run concurrently for different directories
- Sessions are named using lowercase-kebab-case (e.g., `dev-ai-config`)

### Conversation Persistence

- Conversations are automatically saved and tied to directory paths
- On startup, you'll be prompted to resume the previous conversation
- Press Enter (default: Yes) to resume, or type 'n' for a fresh chat
- All conversation history is shared with your host Kiro CLI installation

### Included Tools

The sandbox includes essential platform engineering tools:

**Infrastructure as Code:**
- OpenTofu (latest)
- terraform-docs (latest)

**AWS:**
- AWS CLI v2
- Kiro CLI (latest)

**SaaS Integration:**
- GitHub CLI (gh)
- Atlassian CLI (acli)
- Scalr CLI

**Development:**
- Python 3 (latest stable via uv)
- uv (Python package manager)

**Utilities:**
- git
- jq
- yq
- yamllint
- shellcheck

### Authentication

**Kiro CLI:**
- Automatically handled via device flow on first run
- Credentials shared with host system

**GitHub CLI:**
- Set `GH_TOKEN` environment variable on your host
- Automatically passed to container

**Other Tools:**
- Atlassian CLI and Scalr CLI authentication to be configured

## Environment Variables

- `GH_TOKEN` - GitHub personal access token for gh CLI authentication

## Directory Structure

```
sandbox/
├── Dockerfile           # Container image definition
├── entrypoint.sh       # Container startup script
├── kiro                # Wrapper script for running sandbox
└── README.md           # This file
```

## Contributing

### Architecture

The sandbox consists of three main components:

1. **Dockerfile** - Defines the container image with all required tools
2. **entrypoint.sh** - Handles authentication and starts Kiro CLI
3. **kiro** - Wrapper script that manages sessions and container lifecycle

### Technical Design

#### Session Naming

Session names are generated from directory paths:
- Remove home directory prefix
- Convert to lowercase
- Replace spaces and slashes with hyphens
- Example: `/Users/simon/dev/My Project` → `dev-my-project`

#### Volume Mounts

The container mounts three key directories:

1. **Working Directory**: `$WORK_DIR` → `/opt/$SESSION_NAME`
   - Your project files
   - Read-write access

2. **Kiro Config**: `~/.kiro` → `/root/.kiro`
   - Kiro CLI configuration
   - Shared with host

3. **Kiro Data**: `~/Library/Application Support/kiro-cli` → `/root/.local/share/kiro-cli`
   - Conversation database
   - Command history
   - Shared with host

#### Container Lifecycle

1. Check if session already running (prevent duplicates)
2. Build image if it doesn't exist
3. Start container with:
   - Unique name based on session
   - Working directory set to session path
   - Auto-remove on exit (`--rm`)
   - Interactive TTY (`-it`)

#### Build Optimization

Dockerfile layers are ordered by change frequency:
1. Base packages (least frequent)
2. AWS CLI, jq, yq
3. terraform-docs
4. GitHub CLI, Atlassian CLI, Scalr CLI
5. uv + Python
6. Kiro CLI (most frequent)
7. Entrypoint script

This ensures efficient caching and faster rebuilds.

### Adding New Tools

To add a new tool to the sandbox:

1. Add installation commands to `Dockerfile`
2. Place in appropriate layer based on update frequency
3. Consider architecture detection for multi-platform support
4. Update the "Included Tools" section in this README

Example:
```dockerfile
RUN ARCH=$(uname -m) && \
    if [ "$ARCH" = "x86_64" ]; then \
        TOOL_ARCH="amd64"; \
    elif [ "$ARCH" = "aarch64" ]; then \
        TOOL_ARCH="arm64"; \
    fi && \
    curl -fsSL "https://example.com/tool-${TOOL_ARCH}" -o /usr/local/bin/tool && \
    chmod +x /usr/local/bin/tool
```

### Adding Authentication Support

To add authentication for a new tool:

1. Determine authentication method (env var, config file, etc.)
2. For environment variables:
   - Add to wrapper script's docker run command
   - Document in "Environment Variables" section
3. For config files:
   - Add volume mount to wrapper script
   - Document in "Authentication" section

### Modifying the Wrapper Script

The `kiro` wrapper script uses functions for maintainability:

- `show_help()` - Display usage information
- `list_sessions()` - Show running sessions
- `stop_session()` - Stop a specific session
- `generate_session_name()` - Convert path to session name
- `check_session_running()` - Prevent duplicate sessions
- `build_image()` - Build image if missing
- `run_container()` - Execute the container

When adding new options:
1. Add to argument parser
2. Update `show_help()` function
3. Add color coding for output consistency

### Color Scheme

The wrapper script uses consistent colors:
- **Blue** - Section headers
- **Magenta** - Highlighted values (paths, names, options)
- **Green** - Success messages
- **Red** - Error messages
- **Yellow** - Warnings (reserved for future use)
- **Cyan** - Reserved for future use

## Troubleshooting

### Image Build Fails

```bash
# Rebuild from scratch
./kiro --rebuild
```

### Session Won't Start

```bash
# Check for existing sessions
./kiro --list

# Stop conflicting session
./kiro --stop <session-name>
```

### Authentication Issues

```bash
# Drop into shell and debug
./kiro --shell

# Check Kiro CLI status
kiro-cli doctor

# Re-authenticate
kiro-cli logout
kiro-cli login --use-device-flow
```
