# WAP to enter marks of 3 subjects from the user and store them 
# in a dictionary. Start with an empty dictionary & add 
# one by one. Use subject name as key & marks as value.

subjects = {}

x = int(input("enter phy: "))
subjects.update({"phy:" : x})

y = int(input("enter math: "))
subjects.update({"math:" : y})

z = int(input("enter che: "))
subjects.update({"che:" : z})




print(subjects)