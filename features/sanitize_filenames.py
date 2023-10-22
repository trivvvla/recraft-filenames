"""Sanitizes file names by removing spaces or dashes at the beginning or end."""

import os
import re
from utilities import file_operations
import config

def feature_sanitize_filenames(path=config.MUSIC_PATH, auto_rename=False):
    data = []

    for root, _, files in os.walk(path):
        for file in files:
            sanitized_file = re.sub(r"^[ -]+|[ -]+$", "", file)
            if sanitized_file != file:
                data.append([
                    root,
                    file,
                    "sanitize_filename",
                    sanitized_file,
                    "Pending"
                ])

    file_operations.process_files(data, auto_rename)
