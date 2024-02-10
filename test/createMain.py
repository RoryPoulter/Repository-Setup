# Test for creating file main.py

def createMainPy(path):
    base_code = """# The main body of the code


if __name__ == "__main__":
    print("Hello world")
"""

    with open(path+r"/main.py", "w") as main_py:
        main_py.write(base_code)


if __name__ == "__main__":
    createMainPy(".")
