#!/bin/bash

echo "[info] Automate conversion of CSV to JSON..."
python3 automate.py

echo "GIT add all..."
git add .

echo "GIT commit..."
git commit -m "update as of $(date)"

echo "GIT publish..."
git push
