import os
from tkinter import *


def gitInit(local_path, remote_repo):
    repo_name = remote_repo.split("/")[4][:-4]
    print(local_path)
    os.system(rf'''echo "# {repo_name}" >> {local_path}\README.md''')
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
    createDirectories(local_path)
    print("------------------\nCreating files")
    open(local_path+r"/.gitignore", "a")
    print("Created file .gitignore")
    if create_main.get():
        open(local_path+r"/src/main.py", "a")
        print("Created main.py")
    gitInit(local_path, remote_repo)


if __name__ == "__main__":

    root = Tk()
    root.title("Repository setup")
    root.geometry("600x400")
    Label(root, text="GitHub Repository Initializer", font=20).pack(pady=5)

    path = StringVar()
    repo = StringVar()
    Label(root, text="Path:").pack(pady=10)
    Entry(root, textvariable=path, width=75).pack()
    Label(root, text="Repo:").pack(pady=10)
    Entry(root, textvariable=repo, width=75).pack()

    create_main = BooleanVar(value=False)
    Checkbutton(root, variable=create_main, text="Create main.py")

    Button(root, text="Setup", command=setupRepository).pack(pady=25)

    root.mainloop()
