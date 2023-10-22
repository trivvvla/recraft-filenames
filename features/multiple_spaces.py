"""List and fix filenames with multiple spaces."""

import os
from utilities.features_utils import process_files
import config

def modify_multiple_spaces(filename):
    """Modifies filenames with multiple spaces."""
    if "  " in filename:
        return " ".join(filename.split())
    return None

def feature_multiple_spaces(path=config.MUSIC_PATH, auto_rename=False):
    """Lists all files that have two or more spaces in their filename."""
    process_files(modify_multiple_spaces, "multiple_spaces", path, auto_rename)
