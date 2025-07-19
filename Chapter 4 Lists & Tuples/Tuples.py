# A built-in data type that lets us create immutable sequences of values
# we cannot change value at any idx

tuple = (2, 1, 3, 1)
print(type(tuple))
print(tuple[0])
print(tuple[1])


# Slicing in tuple is same as lists
tup2 = (1, 2, 3, 4)
print(tup2[1:3])

# Tuple Methods
tup = (1,2, 4 ,7, 9, 3,5, 3)
print(tup)

print(tup.index(2)) #returns idx of first occurence

print(tup.count(3)) #counts total occurences
