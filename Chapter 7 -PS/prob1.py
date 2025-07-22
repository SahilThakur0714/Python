# Write a program to greet all the person names stored in a list 'l' and which starts
# with S.
# l = ["Harry", "Soham", "Sachin", "Rahul"]


l = ["Harry", "Soham", "Sachin", "Rahul"]

for name in l:
    if(name.startswith("S")):
        print("hello", name)

# Write a program to find whether a given number is prime or not.
n = int(input("enter a number: "))
power=int(n**(1/2))
cnt=0
for i in range(2,power+1):
    if(n%i) == 0:
        cnt+=1

    if cnt>1:
        print("number is not prime")
else:
    print("number is prime")

            # OR

for i in range(2, n):
    if(n%i)==0:
        print("Number is not prime")
        break
else:
    print("Number is prime")

# print numbers between 2 to n
for num in range(2, n+1):
    for i in range(2,num):
        if num % i == 0:
            break
    else:
        print(num,"is prime")
