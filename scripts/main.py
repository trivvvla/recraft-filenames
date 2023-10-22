import os
import importlib
from utilities import file_operations
from config import *
from termcolor import colored

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
    print(f"{colored('Current working directory:', 'blue')} {MUSIC_PATH}\n")

    subdirs = [dir_name for dir_name in os.listdir(MUSIC_PATH) if os.path.isdir(os.path.join(MUSIC_PATH, dir_name)) and dir_name not in IGNORE_DIRS]
    
    if not subdirs:
        print("No additional subdirectories found.")
        return

    print(colored('List of subdirectories:', 'blue'))
    for idx, dir_name in enumerate(subdirs, 1):
        print(f"{colored(str(idx), 'yellow')}. {dir_name}")
    print("\nEnter the numbers of the directories you wish to exclude (comma separated), or press enter to continue without excluding any:")

    excluded_dirs = input().strip().split(',')
    for dir_num in excluded_dirs:
        try:
            IGNORE_DIRS.append(subdirs[int(dir_num) - 1])
        except (ValueError, IndexError):
            # In case the input number isn't valid, we simply ignore it.
            pass

    print(f"Excluded directories: {colored(IGNORE_DIRS, 'red')}\n")

def display_menu():
    """Display the available operations."""
    print("\n" + colored('➜ FEATURE SELECTION', 'green').center(60, '-'))
    print("Please choose an operation:")
    for idx, module in enumerate(feature_modules, 1):
        # Assuming each feature module has a `__doc__` string describing its purpose
        print(f"{colored(str(idx), 'yellow')}. {module.__doc__}")
    print(f"{colored(str(len(feature_modules) + 1), 'yellow')}. Run all features")
    print(f"{colored(str(len(feature_modules) + 2), 'yellow')}. Exit")

def main():
    confirm_directories()

    while True:
        display_menu()
        try:
            choice = int(input(f"\nEnter your choice (1-{len(feature_modules) + 2}): "))

            if choice == len(feature_modules) + 1:  # Run all features
                for module in feature_modules:
                    # Get the function name dynamically and run it
                    function_to_run = getattr(module, f"{FEATURE_PREFIX}{module.__name__.split('.')[-1]}")
                    function_to_run()
            elif choice > 0 and choice <= len(feature_modules):
                function_to_run = getattr(feature_modules[choice - 1], f"{FEATURE_PREFIX}{feature_modules[choice - 1].__name__.split('.')[-1]}")
                function_to_run()
            elif choice == len(feature_modules) + 2:  # Exit
                break
            else:
                print(colored("\nInvalid choice. Please select from the menu.", 'red'))
        except ValueError:
            print(colored("\nInvalid input. Please select a number from the menu.", 'red'))

if __name__ == "__main__":
    main()
