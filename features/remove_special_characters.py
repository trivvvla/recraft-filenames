"""List and fix filenames containing characters not in the whitelist."""

import os
from formatters import format_output
from utilities import file_operations
from utilities.file_operations import process_files
import config

ALLOWED_CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789()|｜.-_&— ,åâéÁèêëËàôðöÖÔÓúúü'í+Æœð"

def feature_remove_special_characters(path=config.MUSIC_PATH, auto_rename=False):
    data = []

    for root, _, files in os.walk(path):
        for file in files:
            new_filename = ''.join([char for char in file if char in ALLOWED_CHARACTERS])
            if new_filename != file:
                data.append([
                    root,
                    file,
                    "check_characters",
                    new_filename,
                    "Pending"
                ])

    file_operations.process_files(data, auto_rename)


