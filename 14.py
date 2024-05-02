# 1. input for 5 ages from the user
# 2. print out the biggest age from the user
# 3. write a function that get name as input from the user until the name "moshe" and return a list of those names

user_ages_str = input("Provide 5 ages separating with space each one: ").split()
user_ages = list(map(int, user_ages_str))
biggest_number = user_ages[0]

for age in user_ages:
    if age > biggest_number:
        biggest_number = age

print(f"The biggest age is: {biggest_number}")

while True:
    user_names = input("Provide names and hit with old 'moshe' when you like ;) ")
    if user_names == "moshe":
        break
print(user_names)



    #if user_ages[0] < age:
     #   biggest_so_far = age
      #  print(biggest_so_far)
       # if biggest_so_far < age:
        #    biggest_so_far = age
         #   print(f"The biggest age is: {biggest_so_far}")
#else:
 #   print(f"The biggest age is: {user_ages[0]}")
 #   else:
 #       biggest_so_far = user_ages[0]
#for age in user_ages:
   # if biggest_so_far < age:
  #      biggest_so_far = age
 #       print(f"The biggest age is: {biggest_so_far}")


# 30 203 342 4 42 30 554 443

#for age in user_ages:
 #   if user_ages[0] < age:
  #      biggest_so_far = age
#if biggest_so_far == user_ages[0]:
 #   print(f"The biggest age is: {user_ages[0]}")
#else:
 #   print(f"The biggest age is: {biggest_so_far}")


