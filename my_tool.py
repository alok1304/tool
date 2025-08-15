# my_tool.py
import sys
import os
import re
import spacy

# Load English NLP model for NER
nlp = spacy.load("en_core_web_sm")

# Regex pattern for "Neither the name of ... nor the"
pattern_neither = re.compile(r"(Neither the name of )(.+?)( nor the)", re.IGNORECASE)

def replace_named_entities(text):
    """
    Replaces PERSON entities with [[6]] placeholder.
    Uses regex for 'Neither the name of' pattern and NER as fallback.
    """
    # First, handle the specific "Neither the name of ..." case
    text = pattern_neither.sub(r"\1[[6]]\3", text)

    # Then, run NER on the remaining text for generic PERSON replacement
    doc = nlp(text)
    new_text = text

    # Replace only PERSON entities, starting from the end to avoid messing up offsets
    for ent in sorted(doc.ents, key=lambda x: x.start_char, reverse=True):
        if ent.label_ == "PERSON":
            new_text = new_text[:ent.start_char] + "[[6]]" + new_text[ent.end_char:]

    return new_text


def process_file(file_path):
    """Read, process, and overwrite a single file."""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    updated_content = replace_named_entities(content)

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
