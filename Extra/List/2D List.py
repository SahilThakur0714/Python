# A 2D list is just a list made up of list

# fruits =     ["apple", "orange", "banana", "coconut"]
# vegetables = ["celery", "carrots", "potaotes"]
# meats =      ["chicken", "fish", "turkey"]

# groceries = [fruits, vegetables, meats]

# OR
groceries = [ ["apple", "orange", "banana", "coconut"],
              ["celery", "carrots", "potaotes"],
              ["chicken", "fish", "turkey"]]

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()

# print(groceries)
# print(groceries[0])
# print(groceries[0][0])
# print(groceries[1])
# print(groceries[1][1])
# print(groceries[2])
# print(groceries[2][2])

