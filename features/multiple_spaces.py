"""List and fix filenames with multiple spaces."""
...
import os
from formatters import format_output
from utilities import file_operations
import config

...
def feature_multiple_spaces(path=config.MUSIC_PATH, auto_rename=False):
    """Lists all files that have two or more spaces in their filename."""

    data = []

    for root, _, files in os.walk(path):
        for file in files:
            if "  " in file:
                new_filename = " ".join(file.split())
                data.append([
                    root,
                    file,
                    "multiple_spaces",
                    new_filename,
                    "Pending"
                ])

    if not auto_rename:
        for i, row in enumerate(data):
            # Extract relative path to supply as an argument to format_prompt
            relative_path = format_output.extract_last_two_dirs(row[0])
            
            user_input = input(format_output.format_prompt(i, data, row, relative_path))
            if user_input.lower() in ("", "y"):
                file_operations.rename_file(row)
            else:
                row[4] = format_output.format_status("Skipped")

        print(format_output.format_data(data))
    else:
        for row in data:
            file_operations.rename_file(row)
