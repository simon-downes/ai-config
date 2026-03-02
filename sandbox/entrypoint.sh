#!/bin/bash

kiro-cli login --use-device-flow 2>&1 | grep -v "Already logged in" || true

# Prompt to resume chat if no arguments provided
if [ $# -eq 0 ]; then
    read -p "Resume previous chat? [Y/n] " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Nn]$ ]]; then
        exec kiro-cli chat
    else
        exec kiro-cli chat --resume
    fi
else
    exec kiro-cli "$@"
fi
