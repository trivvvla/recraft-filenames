"""List and fix filenames containing characters not in the whitelist."""

from utilities.features_utils import process_files
import config

ALLOWED_CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789()|｜.-_&— ,åâéÁèêëËàôðöÖÔÓúúü'í+Æœð"

def modify_check_characters(filename):
    new_filename = ''.join([char for char in filename if char in ALLOWED_CHARACTERS])
    return new_filename if new_filename != filename else None

def feature_remove_special_characters(path=config.MUSIC_PATH, auto_rename=False):
    process_files(modify_check_characters, "check_characters", path, auto_rename)
