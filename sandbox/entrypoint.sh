#!/bin/bash

kiro-cli login --use-device-flow 2>&1 | grep -v "Already logged in" || true

cd "/opt/$SESSION_NAME" || exit 1

exec kiro-cli "$@"
