# Write a python function to print first n lines of the following pattern:
# ***
# **
# * for n=3

def pattern(n):
    if(n==0):
        return ""
    else:
        print("*"*n)
        return pattern(n-1)
    
pattern(3)

# Write a python function to remove a given word from a list ad strip 
# it at the same time.


def remvoe(list, word):
    w = []
    for i in list:
        if not(i==word):
            w.append(i.strip(word))
    return w

    
name = ["Harry","Rohan","Potter","Ron","Hermione"]

print(remvoe(name,"on"))
print(remvoe(name,"Rohan"))