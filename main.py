# for Bonus Question Q11


# write all function definitions here




if __name__ == '__main__':
    # write the main code here
    import os
import re
from collections import Counter
import sys
SKILLS = [
    "python", "sql", "excel", "power bi", "tableau",
    "machine learning", "data analysis", "pandas",
    "numpy", "statistics", "communication"
]

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)
    return text

def extract_skills(text):
    found = []
    for skill in SKILLS:
        if skill in text:
            found.append(skill)
    return found

def read_files_from_folder(folder_path):
    all_text = ""

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if filename.endswith(".txt"):
            with open(file_path, "r", encoding="utf-8") as file:
                all_text += file.read() + " "

    return all_text

def main():
    if len(sys.argv) < 2:
        print("Usage: python skills_extractor.py <folder_path>")
        return

    folder_path = sys.argv[1]

    if not os.path.exists(folder_path):
        print("Folder does not exist.")
        return

    print("Reading files...")

    text = read_files_from_folder(folder_path)
    text = clean_text(text)

    skills_found = extract_skills(text)
    skill_counts = Counter(skills_found)

    print("\nTop Skills Demanded:\n")

    for skill, count in skill_counts.most_common(10):
        print(f"{skill.title()} - {count}")

if __name__ == "__main__":
    main()
