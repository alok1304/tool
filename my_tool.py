# my_tool.py
import sys
import os
import spacy

# Load English NLP model for NER
nlp = spacy.load("en_core_web_sm")

def replace_named_entities(text):
    doc = nlp(text)
    new_text = text
    # Replace only PERSON entities, starting from the end
    for ent in sorted(doc.ents, key=lambda x: x.start_char, reverse=True):
        if ent.label_ == "PERSON":  # Check if the entity type is PERSON
            new_text = new_text[:ent.start_char] + "[[6]]" + new_text[ent.end_char:]
    return new_text


def process_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    updated_content = replace_named_entities(content)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(updated_content)

    print(f"[TOOL] Replaced named entities in {file_path}")

def run_tool(target_path):
    if os.path.isfile(target_path):
        process_file(target_path)
    elif os.path.isdir(target_path):
        for filename in os.listdir(target_path):
            file_path = os.path.join(target_path, filename)
            if os.path.isfile(file_path):
                process_file(file_path)
    else:
        print("[TOOL] Path does not exist!")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python my_tool.py /path/to/file-or-folder")
    else:
        run_tool(sys.argv[1])
