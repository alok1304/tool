# my_tool.py
import sys
import os
import re

# Regex pattern to match "Neither the name of <NAME> nor the"
pattern = re.compile(r"(Neither the name of )(.+?)( nor the)", re.IGNORECASE)

def replace_neither_name(text, default_words=6):
    """
    Replace text between 'Neither the name of' and 'nor the' with [[N]].
    """
    return pattern.sub(rf"\1[[{default_words}]]\3", text)

def process_file(file_path):
    """Process a single file."""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    updated_content = replace_neither_name(content)

    if updated_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(updated_content)
        print(f"[TOOL] Updated: {file_path}")

def run_tool(target_path):
    """Process a file or all files in a folder recursively."""
    if os.path.isfile(target_path):
        process_file(target_path)
    elif os.path.isdir(target_path):
        for root, _, files in os.walk(target_path):
            for filename in files:
                file_path = os.path.join(root, filename)
                if os.path.isfile(file_path):
                    process_file(file_path)
    else:
        print("[TOOL] Path does not exist!")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python my_tool.py /path/to/file-or-folder")
    else:
        run_tool(sys.argv[1])
