# When a function calls itself repeatedly

def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)

show(3)

# factotrial using recursion
def fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * fact(n-1)

print(fact(5))