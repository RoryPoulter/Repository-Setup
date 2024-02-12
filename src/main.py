import os
from tkinter import *
from tkinter import messagebox


def verifyInputs(local_path, remote_repo):
    if "" in (local_path, remote_repo):
        messagebox.showerror("Error", "Empty fields")
        return False
    dir_exists = os.path.exists(local_path)
    if not dir_exists:
        messagebox.showerror("Error", f"Directory {local_path} does not exist")
        return False
    link = remote_repo.split("/")
    if link[0] != "https:":
        messagebox.showerror("Error", "Invalid remote repository")
        return False
    if link[1] != "":
        messagebox.showerror("Error", "Invalid remote repository")
        return False
    if link[2] != "github.com":
        messagebox.showerror("Error", "Invalid remote repository")
        return False
    if link[4][-4:] != ".git":
        messagebox.showerror("Error", "Invalid remote repository")
        return False


def createReadme(local_path, remote_repo):
    repo_name = remote_repo.split("/")[4][:-4]
    with open(local_path+r"/README.md", "w") as readme:
        readme.write(f"# {repo_name}")
    print("Created file README.md")


def createMainPy(local_path):
    base_code = """# The main body of the code


if __name__ == "__main__":
    print("Hello world")
"""

    with open(local_path+r"/src/main.py", "w") as main_py:
        main_py.write(base_code)
    print("Created main.py")


def gitInit(local_path, remote_repo):
    os.system(rf'git init {local_path}')
    os.system(rf'git -C {local_path} add README.md')
    os.system(rf'git -C {local_path} commit -m "first commit"')
    os.system(rf'git -C {local_path} branch -M main')
    os.system(rf'git -C {local_path} remote add origin {remote_repo}')
    os.system(rf'git -C {local_path} push -u origin main')


def createDirectories(local_path):
    print("------------------\nCreating directories")
    for directory in (r"\src", r"\test", r"\doc", r"\.build"):
        try:
            os.mkdir(local_path + directory)
        except FileExistsError:
            print(f"Directory {directory} already exists")
        else:
            print(f"Created directory {directory}")


def setupRepository():
    local_path = path.get().strip('"')
    remote_repo = repo.get()
    valid = verifyInputs(local_path, remote_repo)
    if not valid:
        return
    createDirectories(local_path)
    print("------------------\nCreating files")
    createReadme(local_path, remote_repo)
    open(local_path+r"/.gitignore", "a")
    print("Created file .gitignore")
    if create_main.get():
        createMainPy(local_path)
    gitInit(local_path, remote_repo)


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
    Label(window, text="Remote Repository (https):", bg="#24292e", fg="#ffffff", font=font).pack(pady=10)
    Entry(window, textvariable=repo, width=75, bg="#24292e", fg="#ffffff", highlightthickness=1,
          highlightbackground="#2b3137").pack()
    Checkbutton(window, variable=create_main, text="Create main.py", bg="#24292e", fg="#ffffff",
                activebackground="#24292e", activeforeground="#ffffff", selectcolor="#24292e", font=font).pack()
    Button(window, text="Setup", command=setupRepository, bg="#2dba4e", fg="#ffffff", font=font,
           activeforeground="#ffffff", activebackground="#2dba4e", borderwidth=0, width=10).pack(pady=25)


if __name__ == "__main__":
    root = Tk()
    path = StringVar()
    repo = StringVar()
    create_main = BooleanVar(value=False)
    setupWindow(root, path, repo, create_main)
    root.mainloop()
