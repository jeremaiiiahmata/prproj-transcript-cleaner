import tkinter as tk
from gui import TranscriptCleanerGUI

def main():

    root = tk.Tk()
    TranscriptCleanerGUI(root)
    root.mainloop()

if  __name__ == "__main__":
    main()