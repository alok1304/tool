# my_tool.py
import sys
import os

def run_tool(target_path):
    print(f"[TOOL] Adding 'Hello' to all .txt files in: {target_path}")
    if not os.path.exists(target_path):
        print("[TOOL] Path does not exist!")
        return

    # Iterate through all files in the given path
    for filename in os.listdir(target_path):
        file_path = os.path.join(target_path, filename)

        # Only modify .txt files
        if os.path.isfile(file_path) and filename.endswith(".txt"):
            with open(file_path, "a") as f:
                f.write("\nHello")
            print(f"[TOOL] Added 'Hello' to {filename}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python my_tool.py /path/to/project")
    else:
        run_tool(sys.argv[1])
