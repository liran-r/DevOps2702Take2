import os
user_name = os.environ.get("user_name")
x = os.path.join("/Users/liranreznik/Desktop", f"{user_name}.txt")
def text_file_creator():
    open(x, "x")

text_file_creator()
