from tkinter import *
from tkinter import messagebox


def success():
    messagebox.showinfo("Success", "Repository successfully created!")


def browseDirectories():
    ...


def setupWindow(window, path, repo, create_main):
    font = "SFMono"
    icon = PhotoImage(file="../res/icon.png")
    window.title("GitHub Repository Initializer")
    window.iconphoto(False, icon)
    window.geometry("600x400")
    window.config(bg="#24292e")
    window.resizable(False, False)

    Label(window, text="GitHub Repository Initializer", font=(font, 20, "bold"), bg="#24292e", fg="#ffffff").pack(pady=5)

    Label(window, text="Directory Path:", bg="#24292e", fg="#ffffff", font=font).pack(pady=10)
    Entry(window, textvariable=path, width=75, bg="#24292e", fg="#ffffff", highlightthickness=1,
          highlightbackground="#2b3137").pack()
    Button(window, text="Browse", bg="#2b3137", fg="#ffffff", borderwidth=0, font=font, width=10,
           activebackground="#2b3137", activeforeground="#ffffff", command=browseDirectories).pack(pady=3)
    Label(window, text="Remote Repository (https):", bg="#24292e", fg="#ffffff", font=font).pack(pady=10)
    Entry(window, textvariable=repo, width=75, bg="#24292e", fg="#ffffff", highlightthickness=1,
          highlightbackground="#2b3137").pack()
    Checkbutton(window, variable=create_main, text="Create main.py", bg="#24292e", fg="#ffffff",
                activebackground="#24292e", activeforeground="#ffffff", selectcolor="#24292e", font=font).pack()
    Button(window, text="Setup", command=success, bg="#2dba4e", fg="#ffffff", font=font, activeforeground="#ffffff",
           activebackground="#2dba4e", borderwidth=0, width=10).pack(pady=25)


if __name__ == "__main__":
    root = Tk()
    path = StringVar()
    repo = StringVar()
    create_main = BooleanVar(value=False)
    setupWindow(root, path, repo, create_main)
    root.mainloop()
