#!/usr/bin/env bash
set -euo pipefail

# AI Config Installation Script
# Copies agents, skills, prompts, and guidance to ~/.kiro/

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
KIRO_DIR="${HOME}/.kiro"

echo "Installing AI configuration to ${KIRO_DIR}..."

# Create target directories if they don't exist
mkdir -p "${KIRO_DIR}/agents"
mkdir -p "${KIRO_DIR}/skills"
mkdir -p "${KIRO_DIR}/prompts"
mkdir -p "${KIRO_DIR}/steering"

# Copy agents
echo "Copying agents..."
cp -r "${SCRIPT_DIR}/agents/"* "${KIRO_DIR}/agents/"

# Copy skills
echo "Copying skills..."
cp -r "${SCRIPT_DIR}/skills/"* "${KIRO_DIR}/skills/"

# Copy prompts
echo "Copying prompts..."
cp -r "${SCRIPT_DIR}/prompts/"* "${KIRO_DIR}/prompts/"

# Copy guidance to steering
echo "Copying guidance..."
cp -r "${SCRIPT_DIR}/guidance/"* "${KIRO_DIR}/steering/"

echo "✓ Installation complete!"
echo ""
echo "Installed:"
echo "  - Agents: ${KIRO_DIR}/agents/"
echo "  - Skills: ${KIRO_DIR}/skills/"
echo "  - Prompts: ${KIRO_DIR}/prompts/"
echo "  - Steering: ${KIRO_DIR}/steering/"
