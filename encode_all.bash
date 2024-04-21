#!/bin/bash

# Change directory to "success"

failed_count=0
done_files=0
file_count=$(find success/* -type f | wc -l)
# Iterate over each file in the directory
for file in success/*; do
    # Run main.py with the file name as the command-line argument
    python main.py $(basename "$file") > /dev/null
    # Check the exit status of the previous command
    if [ $? -ne 0 ]; then
        # Increment the counter and print the name of the failed file
        ((failed_count++))
        echo "Failed: $file"
        echo "$file" >> failed_files.txt
    fi
    ((done_files++))
    echo "$done_files/$file_count"
done

echo "Total failed files: $failed_count"