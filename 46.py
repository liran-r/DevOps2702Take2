def get_age():
    current_age = int(input("Enter your age: "))
    if current_age <= 17:
        raise BaseException("age can not be under 18")


try:
    get_age()
except BaseException as e:
    print(e.args)

