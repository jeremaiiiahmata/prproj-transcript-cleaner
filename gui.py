import tkinter as tk
from tkinter import filedialog, messagebox

from processor import process_folder


class TranscriptCleanerGUI:

    def __init__(self, root):
        self.root = root

        self.folder_path = tk.StringVar()
        self.youtube_link = tk.StringVar()

        self.setup_window()
        self.build_ui()

    def setup_window(self):
        self.root.title("Premiere Pro Transcript Cleaner")
        self.root.geometry("700x320")
        self.root.resizable(False, False)
        self.root.configure(bg="#f5f5f5")

    def build_ui(self):

        # ---------- Title ----------
        title = tk.Label(
            self.root,
            text="Premiere Pro Transcript Cleaner",
            font=("Segoe UI", 20, "bold"),
            bg="#f5f5f5"
        )
        title.pack(pady=(20, 10))

        subtitle = tk.Label(
            self.root,
            text="Clean Adobe Premiere transcript exports in one click.",
            font=("Segoe UI", 10),
            fg="gray30",
            bg="#f5f5f5"
        )
        subtitle.pack()

        # ---------- Main Frame ----------
        frame = tk.Frame(self.root, bg="#f5f5f5")
        frame.pack(fill="both", expand=True, padx=30, pady=20)

        # Folder
        tk.Label(
            frame,
            text="Transcript Folder",
            font=("Segoe UI", 10, "bold"),
            bg="#f5f5f5"
        ).grid(row=0, column=0, sticky="w")

        folder_entry = tk.Entry(
            frame,
            textvariable=self.folder_path,
            width=60
        )
        folder_entry.grid(
            row=1,
            column=0,
            padx=(0, 10),
            pady=5,
            sticky="ew"
        )

        browse_btn = tk.Button(
            frame,
            text="Browse",
            command=self.browse_folder
        )
        browse_btn.grid(row=1, column=1)

        # YouTube Link
        tk.Label(
            frame,
            text="YouTube Link (Optional)",
            font=("Segoe UI", 10, "bold"),
            bg="#f5f5f5"
        ).grid(row=2, column=0, sticky="w", pady=(20, 0))

        yt_entry = tk.Entry(
            frame,
            textvariable=self.youtube_link,
            width=60
        )
        yt_entry.grid(
            row=3,
            column=0,
            columnspan=2,
            sticky="ew",
            pady=5
        )

        # Clean Button
        clean_btn = tk.Button(
            frame,
            text="Clean Transcripts",
            command=self.clean_transcripts,
            bg="#5cb85c",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            padx=10,
            pady=8,
            cursor="hand2"
        )
        clean_btn.grid(
            row=4,
            column=0,
            columnspan=2,
            pady=30
        )

        frame.columnconfigure(0, weight=1)

        # Footer
        footer = tk.Label(
            self.root,
            text="Made by @jeremaiiiahmata",
            font=("Segoe UI", 8),
            fg="gray40",
            bg="#f5f5f5"
        )
        footer.pack(side="bottom", pady=10)

    def browse_folder(self):
        folder = filedialog.askdirectory()

        if folder:
            self.folder_path.set(folder)

    def clean_transcripts(self):

        folder = self.folder_path.get()

        if not folder:
            messagebox.showerror(
                "Error",
                "Please select a transcript folder."
            )
            return

        try:
            count = process_folder(
                folder,
                self.youtube_link.get()
            )

            messagebox.showinfo(
                "Success",
                f"Successfully cleaned {count} transcript(s)."
            )

        except Exception as e:
            messagebox.showerror(
                "Error",
                str(e)
            )