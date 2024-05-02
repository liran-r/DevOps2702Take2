# 1
# def divide_by_zero():
#     a = 1 / 0


# 2
# try:
#    divide_by_zero()
# except BaseException as e:
#    print(e.args)

# 3

# try:
#    x = 1
# finally:
#    print("finally")
# No problem with the code as you just print string

# 4
# All types of exeptions can be caught by "Except:" handler.

# 5 It is bad practice because it gives partial info.

# 6 except ZeroDivisionError can caught error of dividing by zero. except IOError can catch error of file that we
# passed in as argument, does not exist or as a different name or the file location path is incorrect.

# 7

# open("words.txt", "x")

# 8

# name = "Liran"
# file = open("words.txt", "a+")
# file.write(name)
# file.close()

# 9

# file = open("words.txt")
# for i in file.readlines():
#    print(i)

# 10

# name = "לירן"
# file = open("words.txt", "a+")
# file.write(name)
# file.close()
# file = open("words.txt")
# for i in file.readlines():
#    print(i)

# 11
#from PIL import Image

#filename = Image.new('RGBA', (60, 30), color = 'blue')
#filename.save("lliran.png")
#with Image.open("lliran.png") as img:
#    img.show("lliran.png")
#    width, height = img.size


