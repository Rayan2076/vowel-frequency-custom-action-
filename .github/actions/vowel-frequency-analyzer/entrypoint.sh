#!/bin/sh

set -e

FILE_PATH="$1"

echo "Starting the Docker-based vowel frequency analyser."
echo "Requested file: $FILE_PATH"

if [ -z "$FILE_PATH" ]; then
    echo "Error: No text file was provided."
    exit 1
fi

if [ ! -f "$FILE_PATH" ]; then
    FILE_PATH="/github/workspace/$FILE_PATH"
fi

if [ ! -f "$FILE_PATH" ]; then
    echo "Error: The requested file could not be found."
    exit 1
fi

python3 /frequency.py "$FILE_PATH"

echo "Custom GitHub Action completed successfully."
