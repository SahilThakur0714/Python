# Write a program to find whether a given username contains less than 10
# characters or not.

username = input("Enter username: ")

if(len(username) < 10):
    print("The username is valid")
else:    
    print("The username contains more than 10 characters")
    print("username is invalid")