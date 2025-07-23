# Functions: Block of statements that perform a specific task
# syntax: def func_name(param1, param2,..):
# func_name(arg1, arg2,..)#function call

def calc_sum(a,b):
    sum = a + b
    # print(sum)
    return sum

print(calc_sum(5,10))

def print_hello():
    print("Hello")

print_hello()
output = print_hello()
print(output)#NOne

# average of 3 numbers
def avg_3(a,b,c):
    return (a+b+c)/3
print(avg_3(1,2,3))
print(avg_3(97,98,95))

# Built-in functions: already written in python

print("I am calm like Bruce", end=" ")
print("I am sharp like Harvey")

len()

# User defined function: written by us
