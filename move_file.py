import os
import shutil

file_name = os.environ.get("file_name")
def move_file():
    file_content = shutil.move(f"/Users/liranreznik/Desktop/{file_name}.txt", "/Users/liranreznik/My Python Stuff/text_files_that_moved/")

move_file()
