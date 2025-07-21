# WAP to check if a number entered by the user is odd or even

num = int(input("Enter a number: "))

if(num % 2 ==0):
    print("number is even")
else:
    print("number is odd")

# WAP to find greatest of 3 numbers entered by the user

a = float(input("Enter a no: "))
b = float(input("Enter a no: "))
c = float(input("Enter a no: "))

if(a > b and a > c):
    print(f"{a} is the greatest number among the 3")
elif(b > a and b > c):
    print(f"{b} is the greatest number among the 3")
elif(c > a and c > b):
    print(f"{c} is the greatest number among the 3")
else:
    print("all numbers are equal")

# WAP to check if a number is a multiple of 7 or not

num1 = int(input("Enter a number: "))

if(num1 % 7 == 0):
    print(f"{num1} is a multiple of 7")
else:
    print(f"{num1} is not a multiple of 7")