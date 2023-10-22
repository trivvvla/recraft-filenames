import os
import importlib
from utilities import file_operations
from config import *
from termcolor import colored
import shutil

FEATURES_DIR = "features"
FEATURE_PREFIX = "feature_"  # Prefix for the function in each feature module

all_files_info = file_operations.collect_filenames_from_path(MUSIC_PATH, IGNORE_DIRS)

# Dynamically load all feature modules in the `features` directory
feature_modules = [
    importlib.import_module(f"{FEATURES_DIR}.{filename[:-3]}")
    for filename in os.listdir(FEATURES_DIR)
    if filename.endswith(".py") and filename != "__init__.py"
]

def confirm_directories():
    """Display the working directory and its subdirectories, allowing users to exclude some."""
    print("\n" + colored('➜ DIRECTORIES SELECTION', 'green').center(60, '-'))
    print(f"📂 {colored('Current working directory:', 'blue')} {MUSIC_PATH}\n")

    subdirs = [dir_name for dir_name in os.listdir(MUSIC_PATH) if os.path.isdir(os.path.join(MUSIC_PATH, dir_name)) and dir_name not in IGNORE_DIRS]
    
    if not subdirs:
        print("No additional subdirectories found.")
        return

    print(colored('❌ Excluded directories:', 'blue'))
    for excluded_dir in IGNORE_DIRS:
        print(f"  • {excluded_dir}")

    print(colored('\nList of directories and subdirectories:', 'blue'))
    for idx, dir_name in enumerate(subdirs, 1):
        print(f"{colored(str(idx), 'yellow')}. {dir_name}")
        
        # Print subdirectories (if any)
        subdir_path = os.path.join(MUSIC_PATH, dir_name)
        if os.path.isdir(subdir_path):
            subdirs_list = [s for s in os.listdir(subdir_path) if os.path.isdir(os.path.join(subdir_path, s))]
            for s_idx, s_dir_name in enumerate(subdirs_list, 1):
                print(f"   {colored(str(idx) + '.' + str(s_idx), 'yellow')}. {s_dir_name}")

    print("\nInstructions:")
    print("- If you want to exclude a directory, type its number (e.g., '2').")
    print("- For subdirectories, use the format '2.1'.")
    print("- Separate multiple entries with commas (e.g., '1,2,2.1').")
    print("\nEnter your exclusions or press enter to skip:")

    excluded_dirs = input().strip().split(',')
    for dir_num in excluded_dirs:
        try:
            if "." in dir_num:
                main_idx, sub_idx = map(int, dir_num.split("."))
                IGNORE_DIRS.append(subdirs_list[sub_idx - 1])
            else:
                IGNORE_DIRS.append(subdirs[int(dir_num) - 1])
        except (ValueError, IndexError):
            # In case the input number isn't valid, we simply ignore it.
            pass


def display_menu():
    """Display the available operations."""
    print("\n" + colored('➜ FEATURE SELECTION', 'green').center(60, '-'))
    print("Please choose an operation:")
    for idx, module in enumerate(feature_modules, 1):
        # Assuming each feature module has a `__doc__` string describing its purpose
        print(f"{colored(str(idx), 'yellow')}. {module.__doc__}")
    print(f"{colored(str(len(feature_modules) + 1), 'yellow')}. Run all features")
    print(f"{colored('q', 'yellow')}. Exit")

    print("\nInstructions:")
    print("- Enter the number corresponding to your desired operation.")
    print("- To exit, select 'q'.")

    return input(f"\nEnter your choice: ")


def main():
    confirm_directories()

    while True:
        choice = display_menu()
        if choice == "q":  # Exit
            break
        try:
            int_choice = int(choice)
            if int_choice == len(feature_modules) + 1:  # Run all features
                for module in feature_modules:
                    # Get the function name dynamically and run it
                    function_to_run = getattr(module, f"{FEATURE_PREFIX}{module.__name__.split('.')[-1]}")
                    function_to_run()
            elif int_choice > 0 and int_choice <= len(feature_modules):
                function_to_run = getattr(feature_modules[int_choice - 1], f"{FEATURE_PREFIX}{feature_modules[int_choice - 1].__name__.split('.')[-1]}")
                function_to_run()
            else:
                print(colored("\nInvalid choice. Please select from the menu.", 'red'))
        except ValueError:
            print(colored("\nInvalid input. Please select a number from the menu or 'q' to exit.", 'red'))

if __name__ == "__main__":
    main()
