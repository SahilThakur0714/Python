# Write a program to find the maximum of the numbers in a list using the 
# reduce function.
from functools import reduce
a = [123,4321,234,12332,93838,3232]

def greater(a,b):
    if(a>b):
        return a
    return b

print(reduce(greater,a))