#!/bin/bash

timestamp=$(date -u +"%Y%m%dT%H%M%SZ")
# echo "$timestamp # Debug

git add .
git commit -m "$timestamp"
git push


