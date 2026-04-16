import os
import re
import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

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
        
        if re.match(r"Unknown", line):
            continue


        cleaned_lines.append(line)

    #Get the youtube link input from user
    yt_link = youtube_link.get()
    
    #Check if user inputted yt link
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

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Dev-Sources\tkinter-designer-output\build\assets\frame0")

window = Tk()

window.title("Premier Pro Transcript Cleaner")
window.geometry("600x400")
window.configure(bg = "#FFFFFF")

folder_path = tk.StringVar()
youtube_link = tk.StringVar()


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 400,
    width = 600,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    144.0,
    400.0,
    fill="#B9F727",
    outline="")

canvas.create_text(
    165.0,
    22.0,
    anchor="nw",
    text="Premier Pro Transcript Cleaner",
    fill="#000000",
    font=("Poppins SemiBold", 24 * -1)
)

canvas.create_text(
    165.0,
    103.0,
    anchor="nw",
    text="File Path:",
    fill="#000000",
    font=("Poppins Medium", 16 * -1)
)

canvas.create_text(
    165.0,
    218.0,
    anchor="nw",
    text="Youtube Link (optional):",
    fill="#000000",
    font=("Poppins Medium", 16 * -1)
)

canvas.create_text(
    485.0,
    381.0,
    anchor="nw",
    text="made by @jeremaiiiahmata",
    fill="#000000",
    font=("Poppins Regular", 7 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    375.5,
    148.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    textvariable=folder_path
)
entry_1.place(
    x=171.0,
    y=131.0,
    width=409.0,
    height=33.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    375.5,
    263.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#DBDBDB",
    fg="#000716",
    highlightthickness=0,
    textvariable=youtube_link
)
entry_2.place(
    x=171.0,
    y=246.0,
    width=409.0,
    height=33.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_browse = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=select_folder,
    relief="flat"
)
button_browse.place(
    x=522.0,
    y=173.0,
    width=63.0,
    height=22.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
clean_transcript_button = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=process_folder,
    relief="flat"
)
clean_transcript_button.place(
    x=316.0,
    y=333.0,
    width=119.0,
    height=22.0
)

window.resizable(False, False)
window.mainloop()
