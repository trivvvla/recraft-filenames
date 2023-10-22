"""Sanitizes file names by removing spaces or dashes at the beginning or end."""

import os
import re
from utilities.features_utils import process_files
import config

def modify_sanitize_filename(filename):
    sanitized_file = re.sub(r"^[ -]+|[ -]+$", "", filename)
    return sanitized_file if sanitized_file != filename else None

def feature_sanitize_filenames(path=config.MUSIC_PATH, auto_rename=False):
    process_files(modify_sanitize_filename, "sanitize_filename", path, auto_rename)
