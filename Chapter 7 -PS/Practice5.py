# WAP to find the sum of first n numbers(using while)
n = 6

sum=0
i=1
while i <=n:
    sum += i
    i +=1
print("totlal sum =",sum)

for i in range(1, n+1):
    sum += i
print("totlal sum =",sum)

# WAP to find the factorial of first n numbers.(using for)

n = 5  

fact = 1

for i in range(1,n+1):
    fact *= i
  
print(fact)