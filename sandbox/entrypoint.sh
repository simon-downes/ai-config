#!/bin/bash

# If SHELL_MODE is set, drop to bash
if [ "$SHELL_MODE" = "1" ]; then
    exec /bin/bash
fi

kiro-cli login --use-device-flow 2>&1 | grep -v "Already logged in" || true

exec kiro-cli chat --agent principal-engineer --resume-picker
