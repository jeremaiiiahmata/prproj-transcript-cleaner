import re

def clean_transcript(file_path, youtube_link=""):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    cleaned = []

    for line in lines:
        line = line.strip()

        if not line:
            continue

        if re.match(r"\d{2};\d{2};\d{2};\d{2} - \d{2};\d{2};\d{2};\d{2}", line):
            continue

        if re.match(r"\d{2}:\d{2}:\d{2}:\d{2} - \d{2}:\d{2}:\d{2}:\d{2}", line):
                    continue

        if re.match(r"V\d+,\s*\d+", line):
            continue

        if re.match(r"Unknown", line):
            continue

        if re.match(r"Speaker 1", line):
                    continue

        cleaned.append(line)

    if youtube_link:
        cleaned.append(f"\n\nVideo Source: {youtube_link}")

    return " ".join(cleaned)