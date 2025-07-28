from functools import reduce

# map
l = [1,2,3,4,5]

sqr = lambda x: x **2

sqrlist = map(sqr, l)
print(list(sqrlist))

# filter
def even(n):
    if(n % 2 == 0):
        return True
    return False

onlyEven = filter(even, l)
print(list(onlyEven))

# reduce
def sum(a,b):
    return a+b
mul = lambda x,y: x*y

print(reduce(sum, l))
print(reduce(mul, l))