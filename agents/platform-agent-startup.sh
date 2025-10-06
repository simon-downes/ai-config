#!/bin/bash

# Platform Engineering Agent Startup Script
# Fetches shared rules and provides startup context

GITHUB_REPO="yourorg/platform-rules"
RULES_BASE_URL="https://raw.githubusercontent.com/$GITHUB_REPO/main"
TEMP_DIR="/tmp/platform-rules"
RULE_FILES=("rules.md" "terraform.md" "python.md")

# Create temp directory
mkdir -p "$TEMP_DIR"

# Fetch shared rules
echo "Fetching shared platform rules..."
for file in "${RULE_FILES[@]}"; do
    if curl -s --fail --max-time 3 "$RULES_BASE_URL/$file" > "$TEMP_DIR/$file"; then
        echo "✓ Downloaded $file"
    else
        echo "⚠ Failed to download $file (using local fallback if available)"
        # Remove empty file if curl failed
        rm -f "$TEMP_DIR/$file"
    fi
done

# Show current context
echo "Platform Engineering Agent Ready"
echo "Working directory: $(pwd)"
echo "Shared rules loaded to: $TEMP_DIR"
