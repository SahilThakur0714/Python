# Print numbers from 1 to 100
for i in range(1,101):
    print(i)

# Print numbers from 100 to 1
for i in range(100,0, -1):
    print(i)

# Print mulriplication table of n 
n = int(input("Enter a number: "))

for i in range(1,11):
    print(f"{n}x{i}= {n*i}")