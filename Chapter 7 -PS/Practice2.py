# Print the elements of the following list using a loop
# [1,4,9,16,25,36,49,64,81,100]

nums = [1,4,9,16,25,36,49,64,81,100]

# traverse: to travel on each element of the list, tuple....
idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1

# Search for a number x in this tuple using loop:
# (1,4,9,16,25,36,49,64,81,100)

nums = (1,4,9,16,25,36,49,64,81,100)

x = 36
i = 0
while i < len(nums):
    if (nums[i] == x):
        print(f"{x} found at index {i}")
    i += 1