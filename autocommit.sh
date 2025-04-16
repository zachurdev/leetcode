#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
timestamp=$(date -u +"%Y%m%dT%H%M%SZ")
git -C "$SCRIPT_DIR" add .
git -C "$SCRIPT_DIR" commit -m "$timestamp"
git -C "$SCRIPT_DIR" push
