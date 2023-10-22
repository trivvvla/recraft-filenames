"""List and replace “—” characters with "-" in filenames."""

import os
from utilities.features_utils import process_files
import config

def modify_replace_dash(filename):
    new_filename = filename.replace("—", "-")
    return new_filename if new_filename != filename else None

def feature_replace_dash(path=config.MUSIC_PATH, auto_rename=False):
    process_files(modify_replace_dash, "replace_dash", path, auto_rename)
