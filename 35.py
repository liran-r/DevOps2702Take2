# my_file = open("/Users/liranreznik/PycharmProjects/pythonProjectDay1/my_file.txt")
# for line in my_file.readlines():
#    print(line)
def get_name():
    file = open("names.txt", "a+")
    names = input(f"Write your name here: ")
    file.write(f"{names}\n")

with open("names.txt") as file:
    for i in file.readlines():
        print(i)

def show_names():
    file = open("names.txt")
    for i in file.readlines():
        print(str(f"Hello {i}"))


get_name()
show_names()

