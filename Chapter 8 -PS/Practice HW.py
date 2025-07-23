# Write a funtion to input a  number, if the num is odd return string"odd"
# and if num is even return string "even"

def odd_even_check(x):
    if(x % 2 !=0):
        print("Odd")
    else:
        print("Even")

odd_even_check(int(input("Enter a number: ")))