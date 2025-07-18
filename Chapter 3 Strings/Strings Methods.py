
name = input("Enter your full name: ")
# phone_number = input("Enter your phone #: ")

result = len(name)
result = name.find("s") #find: to find the first occurence and gives its index
result = name.rfind("a") #rfind: to find the last occurence if python counldn't found any, it will return -1
name = name.capitalize() #capitalize: to capitalize first letter/character of the sentence
name = name.upper() #upper: COnverts all the letters into uppercase
name = name.lower()
# name = name.replace("a", "o") #replace: replace all a with o
# name = name.startswith("sa")
# name = name.endswith("hil")
result = name.isdigit() #isdigit: it returns True if string only have digits otherwise False
result = name.isalpha() #isalpha: it returns true if string only have alphabets otherwise false also if you gave space
# result = phone_number.count("-") #count: counts the number of occurence
# result = phone_number.replace("-", " ") #replace: it replace the string with other string

# print(help(str)) #it will show you all the other bunch of methods

print(name)
print(result)
