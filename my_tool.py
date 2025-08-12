import sys
import os

def replace_word_in_file(file_path, old_word, new_word):
    with open(file_path, "r") as f:
        content = f.read()

    if old_word in content:
        content = content.replace(old_word, new_word)
        with open(file_path, "w") as f:
            f.write(content)
        print(f"[TOOL] Replaced '{old_word}' with '{new_word}' in {file_path}")
    else:
        print(f"[TOOL] No occurrences of '{old_word}' found in {file_path}")

def run_tool(target_path, old_word, new_word):
    if os.path.isfile(target_path):
        replace_word_in_file(target_path, old_word, new_word)

    elif os.path.isdir(target_path):
        for filename in os.listdir(target_path):
            file_path = os.path.join(target_path, filename)
            if os.path.isfile(file_path):  # ✅ No extension restriction now
                replace_word_in_file(file_path, old_word, new_word)
    else:
        print("[TOOL] Path does not exist!")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python my_tool.py /path/to/file-or-folder old_word new_word")
    else:
        run_tool(sys.argv[1], sys.argv[2], sys.argv[3])
