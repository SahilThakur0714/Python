# A list contains the multiplication table of 7. write a program to convert 
# it to vertical string of same numbers.

table =[str(7*i) for i in range(1,11)]

s = "\n".join(table)
print(s)

# Write a program to filter a list of numbers which are divisible by 5.
def divisible(n):
    if(n % 5 == 0):
        return True
    return False

tables =[(7*i) for i in range(1,11)]
f = list(filter(divisible,tables))
print(f)