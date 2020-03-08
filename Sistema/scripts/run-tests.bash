#!/usr/bin/env bash
set -e
cd "${0%/*}/.."

echo "Running tests"
echo "................"

python -m unittest
if [ $? -eq 0 ]
    then
    echo "All tests passed"
    exit 0
else
    exit 1
fi
