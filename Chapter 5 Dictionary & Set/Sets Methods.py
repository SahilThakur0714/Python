# set is mutable but its elements are immutable

collection = {"hello", "apna college", "world"}
collection.add(1)
collection.add(2)
collection.add(2)

collection.remove(1)
collection.add("apna college")
# collection.add([1, 2, 3])
collection.add((1, 2, 3))

# collection.clear()
collection.pop() 
# collection.pop()

# print(len(collection))
print(collection)