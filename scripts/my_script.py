print("Hello")

file_text = """
Hello world
How are you?
I am great!"""


with open("../artifacts/my_text_file.txt", "x") as f:
    f.write(file_text)
