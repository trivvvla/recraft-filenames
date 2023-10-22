import os
from collections import defaultdict
from termcolor import colored

def extract_last_two_dirs(path):
    """Extracts the last two directories from a given path."""
    parts = path.rstrip('/').split('/')
    return '/'.join(parts[-2:]) if len(parts) > 1 else parts[0]

def format_data(data):
    """Formats the data into a table."""
    grouped_data = defaultdict(list)
    modified_files_count = sum(1 for row in data if row[3] == "Replaced")

    banner = f"🎉 Processed Files: {len(data)} | Modified Files: {modified_files_count} 🎉"
    banner_separator = "-" * len(banner)

    formatted_output = "\n" + banner_separator + "\n" + banner + "\n"

    folder_colors = ["blue", "yellow", "red", "green", "purple", "orange", "brown"]
    current_color_index = 0

    for folder, files in grouped_data.items():
        formatted_output += f"{colored('📁', folder_colors[current_color_index])} {folder}\n"
        for file in files:
            status = file[3]
            formatted_output += f"{colored('🟨', folder_colors[current_color_index])} Current: {file[0]}\n"
            if status == "Replaced":
                formatted_output += f"✅ New:      {file[2]}\n\n"
            else:
                formatted_output += f"❌ New:      {file[0]}\n\n"

        current_color_index = (current_color_index + 1) % len(folder_colors)

    return formatted_output.rstrip()

def format_prompt(i, data, row):
    """Formats the prompt for user input."""
    current_file = f"🔳 {row[1]}"
    new_file = f"⬜ {row[3]}"
    return (
        f"{current_file}\n{new_file}\n"
        f"{colored(i+1, 'cyan')} / {colored(len(data), 'cyan')} | ? (y/n) [y] "
    )

def format_status(status):
    """Formats the status."""
    status_map = {
        "Replaced": colored("✓", "green"),
        "Skipped": colored("✗", "red"),
    }
    return status_map.get(status, status)

