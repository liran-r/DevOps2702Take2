import os
file_name = os.environ.get("file_name")
def read_txt_file():
    file_content = open(f"/Users/liranreznik/Desktop/{file_name}"".txt", "r")
    print(file_content.read())

read_txt_file()