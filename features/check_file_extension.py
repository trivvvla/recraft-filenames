"""Lists all files that do not have known audio formats as their extension."""

import os
from utilities import file_operations
import config

KNOWN_AUDIO_FORMATS = ["wav", "mp3", "flac", "aac", "ogg", "wma", "m4a"]

def feature_check_file_extension(path=config.MUSIC_PATH, auto_rename=False):
    data = []

    for root, _, files in os.walk(path):
        for file in files:
            ext = file.split('.')[-1].lower()
            if ext not in KNOWN_AUDIO_FORMATS:
                data.append([
                    root,
                    file,
                    "invalid_extension",
                    file,  # No renaming here as it's just a check
                    "Pending"
                ])

    file_operations.process_files(data, auto_rename)
