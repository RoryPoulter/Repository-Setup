from tkinter import *
from tkinter import filedialog


def browseDirectories():
    directory = '"' + filedialog.askdirectory() + '"'
    path.set(directory)
    print(directory)


root = Tk()
root.geometry("600x300")

path = StringVar()

Button(root, text="Browse", command=browseDirectories).pack(pady=15)
Entry(root, textvariable=path, width=75).pack()
root.mainloop()
