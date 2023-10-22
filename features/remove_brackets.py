"""List and remove content within brackets in filenames."""

import re
from utilities.features_utils import process_files
import config

def modify_remove_brackets(file):
    bracket_pattern = re.compile(r'\[.*?\]')
    if re.search(bracket_pattern, file):
        return re.sub(bracket_pattern, '', file).strip()
    return None

def feature_remove_brackets(path=config.MUSIC_PATH, auto_rename=False):
    process_files(modify_remove_brackets, "remove_brackets", path, auto_rename)