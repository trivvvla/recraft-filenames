import os
import importlib
from utilities import file_operations
from config import *

FEATURES_DIR = "features"
FEATURE_PREFIX = "feature_"  # Prefix for the function in each feature module

all_files_info = file_operations.collect_filenames_from_path(MUSIC_PATH, IGNORE_DIRS)

# Dynamically load all feature modules in the `features` directory
feature_modules = [
    importlib.import_module(f"{FEATURES_DIR}.{filename[:-3]}")
    for filename in os.listdir(FEATURES_DIR)
    if filename.endswith(".py") and filename != "__init__.py"
]

def display_menu():
    """Display the available operations."""
    print("\nPlease choose an operation:")
    for idx, module in enumerate(feature_modules, 1):
        # Assuming each feature module has a `__doc__` string describing its purpose
        print(f"{idx}. {module.__doc__}")
    print(f"{len(feature_modules) + 1}. Run all features")
    print(f"{len(feature_modules) + 2}. Exit")

def main():
    while True:
        display_menu()
        try:
            choice = int(input(f"Enter your choice (1-{len(feature_modules) + 2}): "))

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
                print("Invalid choice. Please select from the menu.")
        except ValueError:
            print("Invalid input. Please select a number from the menu.")

if __name__ == "__main__":
    main()

