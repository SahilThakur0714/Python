# Write a program using functions to find greatest of three numbers.

def great_of_3(a,b,c):
    if(a>b and a>c):
        print(a, "is the greatest")
    elif(b > a and b>c):
        print(b , "is the greatest")
    elif(c>b and c>a):
        print(c , "is the greatest")
    else:
        print("all are equal")
    return

great_of_3(6,6,6)

# Write a python program using function to convert Celsius to Fahrenheit.

def convertion(c):
    f = ((c*9)/5)+32
    print(f)
    return

convertion(7)