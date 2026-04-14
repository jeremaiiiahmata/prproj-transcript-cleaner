import os
import re
import tkinter as tk
from tkinter import filedialog, messagebox

def clean_transcript(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    cleaned_lines = []

    for line in lines:
        line = line.strip()

        if not line:
            continue

        if re.match(r"\d{2};\d{2};\d{2};\d{2} - \d{2};\d{2};\d{2};\d{2}", line):
            continue

        if re.match(r"V\d+,\s*\d+", line):
            continue

        cleaned_lines.append(line)

    yt_link = youtube_link.get()
    
    if not youtube_link  == "":
        cleaned_lines.append(f"\n\nVideo Source : {yt_link}")


    return " ".join(cleaned_lines)


def select_folder():
    folder = filedialog.askdirectory()
    folder_path.set(folder)


def process_folder():
    base_dir = folder_path.get()

    if not base_dir:
        messagebox.showerror("Error", "Please select a folder first.")
        return

    for root, dirs, files in os.walk(base_dir):
        for filename in files:
            if filename.endswith(".txt") and not filename.startswith("cleaned_"):
                file_path = os.path.join(root, filename)

                cleaned_text = clean_transcript(file_path)

                output_path = os.path.join(root, f"cleaned_{filename}")

                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(cleaned_text)

    messagebox.showinfo("Done", "All transcripts cleaned!")



root = tk.Tk()
root.title("Transcript Cleaner")
root.geometry("400x200")

folder_path = tk.StringVar()
youtube_link = tk.StringVar()


tk.Label(root, text="Select Folder:", font=("Arial", 12)).pack(pady=10)

tk.Entry(root, textvariable=folder_path, width=40).pack(pady=5)

tk.Entry(root, textvariable=youtube_link, width= 40).pack(pady=5)

tk.Button(root, text="Browse", command=select_folder).pack(pady=5)

tk.Button(root, text="Clean Transcripts", command=process_folder).pack(pady=20)


root.mainloop()