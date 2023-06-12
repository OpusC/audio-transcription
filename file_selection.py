import tkinter
import tkinter as tk
from tkinter import filedialog
import os

root = tkinter.Tk()
root.withdraw() # hides tkinter window

def search_for_file_path():
    currdir = os.getcwd()
    tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title="Please select a folder")
    if len(tempdir) > 0:
        print(f"You chose {tempdir}")
        return tempdir

