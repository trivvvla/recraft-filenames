import os
import shutil
from formatters import format_output
import config

def collect_filenames_from_path(path, ignore_dirs=[]):
    all_files = []

    for root, dirs, files in os.walk(path):
        # Skip directories in ignore_dirs
        dirs[:] = [d for d in dirs if d not in ignore_dirs]

        for file in files:
            all_files.append((root, file))

    return all_files

def rename_file(row):
    src = os.path.join(row[0], row[1])  # root directory now comes from the row
    dst = os.path.join(row[0], row[3])  # destination is in the same root directory
    try:
        move(src, dst)
        row[4] = format_output.format_status("Replaced")
    except FileNotFoundError:
        print(f"Error: Source file not found: {src}")
        row[4] = format_output.format_status("Error")

def move(src, dst):
    """Moves a file from one location to another."""
    if os.path.exists(dst):
        os.remove(dst)
    shutil.copy2(src, dst)
    os.remove(src)

def process_files(data, auto_rename):
    if not auto_rename:
        for i, row in enumerate(data):
            user_input = input(format_output.format_prompt(i, data, row))
            if user_input.lower() in ("", "y"):
                rename_file(row)
            else:
                row[4] = format_output.format_status("Skipped")
        print(format_output.format_data(data))
    else:
        for row in data:
            rename_file(row)

