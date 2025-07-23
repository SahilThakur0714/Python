# Write a recursive function to calculate the sum of first n natural
#  numbers.

def sum_of_naturals(n):
    if(n == 0):
        return 0
    else:
        return (sum_of_naturals(n-1)) + n

print(sum_of_naturals(5))

# Write a recursive function to print all elements in a list.
# Hint : use list & index as parameters.


def list_elements(list, idx):
    if(idx == len(list)):
        return 
    print(list[idx])
    list_elements(list, idx+1)

nums = [1, 2, 3, 4, 5]

list_elements(nums,0)

