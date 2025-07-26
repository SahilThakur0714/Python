# "del" keyword: used to delete object properties or object itself
# syntax: del s1.name
# del s1

class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Sahil")
print(s1.name)
del s1
print(s1.name)