#A

x = 40
y = 30
if x > y:
    print("BIG")
else:
    print("small")

#B

for a in range(5):
    print(a)

#C

season = 3
if season == 1:
    print("summer")
elif season == 2:
    print("winter")
elif season == 3:
    print("fall")
elif season == 4:
    print("spring")

#D
#it will run 10 times and it will print 10

#E

age = 25
first_letter_of_last_name = "R"
dollar_to_shekel = 3.70
flew = True
apartment_number = 4
print(f"my age is {age}, my first letter of my last name is {first_letter_of_last_name}, to dollar to shekel today is {dollar_to_shekel}, did I ever flew? {flew}, my apartment number is {apartment_number}")
print(age + dollar_to_shekel)

#F
phone_num = input("Please provide your phone number")
print(f"Your phone number is {phone_num}")

#G

def printHello():
        print("hello")
def calculat():
        print(5 + 3.2)

#h
def name():
    name = input("Type your name: ")
    print(name)
def num():
    number = input("Type a number: ")
    print(int(number) / 2)

name()
num()

#I
def sum():
    first_number = input("First number: ")
    second_number = input("Second number: ")
    print(int(first_number) + int(second_number))

def space():
    first_string = input("First string: ")
    second_string = input("Second string: ")
    print(f"{first_string} {second_string}")

sum()
space()




#hashtag = "#"
#for a in hashtag:
#    print(hashtag)
#    a = hashtag + "#"
#    for b in range(5):
#        print(a)
#        a = a + "#"





