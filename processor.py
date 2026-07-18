import os
from cleaner import clean_transcript


def process_folder(folder, youtube_link=""):
    processed = 0

    for root, _, files in os.walk(folder):
        for filename in files:
            if filename.endswith(".txt") and not filename.startswith("cleaned_"):

                file_path = os.path.join(root, filename)

                cleaned = clean_transcript(file_path, youtube_link)

                output = os.path.join(root, f"cleaned_{filename}")

                with open(output, "w", encoding="utf-8") as f:
                    f.write(cleaned)

                processed += 1

    return processed