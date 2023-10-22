"""Lists all files that do not have known audio formats as their extension."""

import os
from utilities.features_utils import process_files
import config

KNOWN_AUDIO_FORMATS = ["wav", "mp3", "flac", "aac", "ogg", "wma", "m4a"]

def modify_check_file_extension(filename):
    """Checks for invalid file extensions."""
    ext = filename.split('.')[-1].lower()
    if ext not in KNOWN_AUDIO_FORMATS:
        return "invalid_extension"  # This is a dummy, as no renaming is done
    return None

def feature_check_file_extension(path=config.MUSIC_PATH, auto_rename=False):
    """Lists all files that do not have known audio formats as their extension."""
    process_files(modify_check_file_extension, "invalid_extension", path, auto_rename)
