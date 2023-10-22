"""List and remove content within brackets in filenames."""

import os
import re
from formatters import format_output
from utilities import file_operations
import config

def feature_remove_brackets(auto_rename=False, path=config.MUSIC_PATH):
    """Lists and renames all files that have text within square brackets in their filename."""

    bracket_pattern = re.compile(r'\[.*?\]')
    data = []

    for root, _, files in os.walk(path):
        for file in files:
            if re.search(bracket_pattern, file):
                new_filename = re.sub(bracket_pattern, '', file).strip()
                data.append([
                    os.path.basename(root),
                    file,
                    "remove_brackets",
                    new_filename,
                    "Pending"
                ])

    if not auto_rename:
        for i, row in enumerate(data):
            user_input = input(format_output.format_prompt(i, data, row))
            if user_input.lower() in ("", "y"):
                file_operations.rename_file(row, root)
            else:
                row[4] = format_output.format_status("Skipped")

        print(format_output.format_data(data))
    else:
        for row in data:
            file_operations.rename_file(row, root)

