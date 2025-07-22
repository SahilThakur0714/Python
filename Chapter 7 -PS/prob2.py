# Write a program to findßlé sum 
# of first n natural numbers using while loop.

n = int(input("enter a number: "))
i = 1
sum = 0
while i <= n:
    sum += i
    i += 1
print(sum)


# Write a program to calculate 
# the factorial of a given number using for loop.

fact = 1
for i in range(1,n+1):
    fact = i * fact
print(fact)

# Write a program to print multiplication table of n using for loops 
# in reversed order.

for i in range(10,0,-1):
    print(i*n)

    # OR
for i in range(1,11):
    print(f"{n} X {11-i} = {n*(11-i)}")