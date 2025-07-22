# Loops are used
# for sequential traversal. For traversing list, string, tuples etc.

nums = [1, 2, 3, 4, 5]

for val in nums:
    if(val == 4):
        print(4, "founded")
        break
    print(val)
else:           #optional- it is used in case of when their break in loop
    print("end")