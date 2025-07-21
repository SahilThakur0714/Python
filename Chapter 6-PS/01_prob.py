# WAP tofind the greatest of 4 numbers entered by the user
num1 = int(input("enter a number1: "))
num2 = int(input("enter a number2: "))
num3 = int(input("enter a number3: "))
num4 = int(input("enter a number4: "))

if(num1 > num2 and num1 > num3 and num1 > num4):
        print(f"{num1} is the greatest number")

elif(num2 >  num1 and num2 > num3 and num2 > num4):
        print(f"{num2} is the grestest number")

elif(num3 >  num1 and num3 > num2 and num3 > num4):
        print(f"{num3} is the grestest number")

elif(num4 >  num1 and num4 > num3 and num4 > num2):
        print(f"{num4} is the grestest number")

else:
    print("all the numbers are equal")
    
