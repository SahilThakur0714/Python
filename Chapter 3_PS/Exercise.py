# validate user input excercise
# 1.username is no more than 12 characters
# 2.username must not contain spaces
# 3.username must not contain digits

username = input("Enter a username: ")

if len(username) > 12:
    print("Your usename can't be more than 12 characters")
elif not username.find(" ") == -1: #username.find(" ") == -1: to check if username has zero spaces or not, if not -1 then it have space
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain numbers")
else:
    print(f"Welcome {username}")