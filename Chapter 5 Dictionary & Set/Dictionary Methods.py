
# syntax: student["score"]["maths"]

student = {
    "name" : "Yash",
    "Subjects": {
        "phy":97,
        "che":98,
        "math": 95
    }
}

print(student.keys()) #returns all keys but not from the nested

print(len(student.keys()))
print(list(student.keys()))
print(len(list(student.keys())))

print(student.values()) #return all values
print(list(student.values())) #we can store list in dict and dict in list

print(student.items()) #returns all(key, val) pairs as tuples
pairs = (list(student.items()))
print(pairs[0])

print(student.get("Subjects")) #"returns the key according to value (mydict.get("key")
# we use get() over dict[] because if the get() no error is show so code after can be executed successfully

new_dict = {"city" : "delhi"}

print(student.update(new_dict)) #insert the specified items to the dictionary
print(student)
 








# myDict.keys( ) #returns all keys
# myDict.values() #returns all values
# myDict.items() #returns all (key, val) pairs as tuples
# myDict.get( ""key"" ) #returns the key according to value
# myDict.update( newDict )#inserts the specified items to the dictionary