"""List and replace “—” characters with "-" in filenames."""

import os
from formatters import format_output
from utilities import file_operations
from utilities.file_operations import process_files
import config

def feature_replace_dash(auto_rename=False, path=config.MUSIC_PATH):
    """Lists and renames all files replacing “—” with "-" in their filename."""

    data = []

    for root, _, files in os.walk(path):
        for file in files:
            new_filename = file.replace("—", "-")
            if new_filename != file:
                data.append([
                    root,
                    file,
                    "replace_dash",
                    new_filename,
                    "Pending"
                ])

    process_files(data, auto_rename)

