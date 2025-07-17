# # P1: Write a program to add two numbers.
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

print(f"Addition of {num1} and {num2} is ",num1 + num2)

# #P2: Write a program to find remainder when a number is divided by z
print(f"Remainder of {num1} divided by {num2} is ",num1 % num2)

#P3: Check the type of variable assigned using input() function
variable_Type = input("Enter input: ")
print(type(variable_Type))

#P4: Use comparison operator to find out whether a given variable  'a' is 
#    greater than 'b' or not. Take a = 34 and b = 80
a = 34
b = 80
print("a is greater than b is:",a>b, "staement")

#P5: Write a program to find an average of two numbers entered by the user
average = (num1 + num2) / 2
print(f"Average of the two numbers {num1} and {num2} is",average)

# P6: Write a program to calculate the square of a number entered by the user
c = float(input("Enter a number: "))
print(f"Square of number {c} is {c**2}")#a**2 is used to calculate the square of any number
