import os
from formatters import format_output
from utilities import file_operations

def process_files(modify_filename_func, tag, path, auto_rename):
    data = []

    for root, _, files in os.walk(path):
        for filename in files:
            new_filename = modify_filename_func(filename)
            if new_filename:
                data.append([
                    root,
                    filename,
                    tag,
                    new_filename,
                    "Pending"
                ])

    if not auto_rename:
        for i, row in enumerate(data):
            relative_path = format_output.extract_last_two_dirs(row[0])
            user_input = input(format_output.format_prompt(i, data, row, relative_path))
            if user_input.lower() in ("", "y"):
                file_operations.rename_file(row)
            else:
                row[4] = format_output.format_status("Skipped")

        print(format_output.format_data(data, tag.replace("_", " ").title()))
    else:
        for row in data:
            file_operations.rename_file(row)
