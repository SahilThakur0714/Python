# This is my first python program
# print("I like cricket!")

# VARIABLES: A container for a value (string, integer, float, boolean)
#                A variable behaves as if it was the value it contains

# Strings: A string is a series of characters.They can include number but 
#          we treat them as characters
# first_name = "Lucifer"
# food = "pizza"
# email = "lucifer123@fake.com"

# print(f"Hello {first_name}")
# print(f"You like {food}")
# print(f"Your email is: {email}")

# Integers
# age = 20
# quantity = 7

# print(f"You are {age} old")
# print(f"you are buying {quantity} items")

# Floats
# price = 10.99
# cgpa = 8.5

# print(f"The price is ${price}")
# print(f"YOur cgpa is {cgpa}")

# Booleans
# is_student = True

# if is_student:
#     print("You are a student")
# else:
#     print("Your are Not a student")

# TYPE CASTING: the process of converting a variable from one data type to another 
#               str(), int(), float(), bool()

# name = "Tony Stark"
# age = 20
# cgpa = 8.5
# is_student = True

# name = bool(name)

# print(name)
# print(type(name))

# cgpa = int(cgpa)

# print(cgpa)
# print(type(cgpa))

# age = str(age)
# age += "1"
# print(age)
# print(type(age))

# print(type(is_student))

# USER INPUT
# input(): A function that prompts the user to enter data
#          Returns the entered data as a string
# Note: When we accept user input we store that input as a string

# name = input("What is your name?: ")
# age = int(input("How old are you?: "))#because of int input will be stored as int
# # age = int(age)

# age = age + 1

# print(f"Welcome! {name}")
# print("Happy Birthday!")
# print(f"You are {age} years old")

# if statements

# age = int(input("Enter your age: "))

# if (age >= 18)  & (age <= 100):
#     print("You are now signed up")
# elif age > 100:
#     print("You are too old to sign up")
# elif age < 0:
#     print("You haven't been born yet")
# else:
#     print("You must be 18+ to sign up")

# name = input("Enter your name: ")

# if name == "":
#     print("You did not type your name")
# else:
#     print(f"Hello {name}!")

is_online = True

if is_online:
    print("User is online")
else:
    print("user is not online")