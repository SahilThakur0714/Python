# Dictionary: are used to store data values in key:value pairs
# They are unordered, mutable & don't allow duplicate keys

info = {
   "name":"apna college",
   "subjects": ["Python", "C", "Java"],
   "topics": ("dict","set"),
    "age":20,
    "is_adult":True,
    12 : 94.4
}

print(info["name"])
print(info["subjects"])
# print(info["surname"])
print(info["topics"])
print(info["age"])
info["name"] = "Sahil thakur"
print(info["name"])

