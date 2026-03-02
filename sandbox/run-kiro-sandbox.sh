#!/bin/bash
set -e

WORK_DIR="${1:-$(pwd)}"
WORK_DIR="$(cd "$WORK_DIR" && pwd)"
HOME_DIR="$HOME"

# Verify work directory is under home directory
if [[ "$WORK_DIR" != "$HOME_DIR"* ]]; then
    echo "Error: Work directory must be under home directory ($HOME_DIR)"
    exit 1
fi

# Generate session name from work directory
RELATIVE_PATH="${WORK_DIR#$HOME_DIR/}"
SESSION_NAME=$(echo "$RELATIVE_PATH" | tr '[:upper:]/ ' '[:lower:]--' | sed 's/--*/-/g')

# Check if container already running for this session
if docker ps --format '{{.Names}}' | grep -q "^kiro-sandbox-${SESSION_NAME}$"; then
    echo "Error: A sandbox session is already running for this directory"
    echo "Container: kiro-sandbox-${SESSION_NAME}"
    exit 1
fi

docker build -t kiro-sandbox . || exit 1

docker run --rm -it \
    --name "kiro-sandbox-${SESSION_NAME}" \
    -v "$HOME/.kiro:/root/.kiro" \
    -v "$HOME/Library/Application Support/kiro-cli:/root/.local/share/kiro-cli" \
    -v "$WORK_DIR:/opt/$SESSION_NAME" \
    -e "SESSION_NAME=$SESSION_NAME" \
    ${GH_TOKEN:+-e "GH_TOKEN=$GH_TOKEN"} \
    kiro-sandbox "${@:2}"
