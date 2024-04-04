#!/bin/bash

# Source directory
SOURCE_DIR="./eswc-kgc-challenge-2024/track2/"

# Destination directory
DEST_DIR="./downloads/track2/"

# Use rsync to merge the directories
rsync -avh --progress "$SOURCE_DIR" "$DEST_DIR"
echo "Merge completed."

# Remove GTFS folders with heterogeneity
rm -r "./downloads/track2/gtfs-madrid-bench/heterogeneity_files"
rm -r "./downloads/track2/gtfs-madrid-bench/heterogeneity_mixed"
rm -r "./downloads/track2/gtfs-madrid-bench/heterogeneity_nested"
rm -r "./downloads/track2/gtfs-madrid-bench/heterogeneity_tabular"

echo "Folders deleted."
