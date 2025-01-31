#!/bin/bash

# Source directory
SOURCE_DIR="./eswc-kgc-challenge-2024/track2/"

# Destination directory
DEST_DIR="./downloads/eswc-kgc-challenge-2024/track2/"

# Use rsync to merge the directories
rsync -avh --progress "$SOURCE_DIR" "$DEST_DIR"
echo "Merge completed."

# Remove GTFS folders with heterogeneity
rm -r "./downloads/eswc-kgc-challenge-2024/track2/gtfs-madrid-bench/heterogeneity_files/"
rm -r "./downloads/eswc-kgc-challenge-2024/track2/gtfs-madrid-bench/heterogeneity_mixed/"
rm -r "./downloads/eswc-kgc-challenge-2024/track2/gtfs-madrid-bench/heterogeneity_nested/"
rm -r "./downloads/eswc-kgc-challenge-2024/track2/gtfs-madrid-bench/heterogeneity_tabular/"

# Remove Track1
rm -r "./downloads/eswc-kgc-challenge-2024/track1/"

echo "Directories deleted."
