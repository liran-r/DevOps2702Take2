my_items = [{"name": "aviel", "age": 33}, {"name": "moshe", "age": 20},
            {"name": "david", "age": 50}]

name = [item["name"] for item in my_items]
print(name)

age = [item["age"] for item in my_items]
print(age)

ageOver30 = [item["age"] for item in my_items if item]

