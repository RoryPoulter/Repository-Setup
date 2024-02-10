from tkinter import *

font = ""


root = Tk()
root.title("GitHub Repository Initializer")
root.geometry("600x400")
root.config(bg="#24292e")

Label(root, text="GitHub Repository Initializer", font=20, bg="#24292e", fg="#ffffff").pack(pady=5)
path = StringVar()
repo = StringVar()
Label(root, text="Path:", bg="#24292e", fg="#ffffff").pack(pady=10)
Entry(root, textvariable=path, width=75, bg="#2b3137", fg="#ffffff").pack()
Label(root, text="Repository (https):", bg="#24292e", fg="#ffffff").pack(pady=10)
Entry(root, textvariable=repo, width=75, bg="#2b3137", fg="#ffffff").pack()
create_main = BooleanVar(value=False)
Checkbutton(root, variable=create_main, text="Create main.py", bg="#24292e", fg="#ffffff",
            activebackground="#24292e", activeforeground="#ffffff", selectcolor="#24292e").pack()
Button(root, text="Setup", command=..., bg="#2dba4e", fg="#ffffff").pack(pady=25)
root.mainloop()
