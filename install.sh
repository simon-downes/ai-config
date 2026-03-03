#!/usr/bin/env bash
set -euo pipefail

# AI Config Installation Script
# Copies agents and skills to ~/.kiro/

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
KIRO_DIR="${HOME}/.kiro"

echo "Installing AI configuration to ${KIRO_DIR}..."

# Create target directories if they don't exist
mkdir -p "${KIRO_DIR}/agents"
mkdir -p "${KIRO_DIR}/skills"

# Copy agents
echo "Copying agents..."
cp -r "${SCRIPT_DIR}/agents/"* "${KIRO_DIR}/agents/"

# Copy skills
echo "Copying skills..."
cp -r "${SCRIPT_DIR}/skills/"* "${KIRO_DIR}/skills/"

echo "✓ Installation complete!"
echo ""
echo "Installed:"
echo "  - Agents: ${KIRO_DIR}/agents/"
echo "  - Skills: ${KIRO_DIR}/skills/"
