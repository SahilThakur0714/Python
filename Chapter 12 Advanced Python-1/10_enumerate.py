l = [1,3,5,7,8,123421]

# index = 0
# for ele in l:
#     print(f"the element at index {index} is {ele}")
#     index += 1

# this can be simplified using enumerate

for index, element in enumerate(l):
     print(f"the element at index {index} is {element}")