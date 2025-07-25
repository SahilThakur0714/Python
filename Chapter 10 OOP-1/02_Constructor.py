# Constructor
# All classes have a function called which is always executed when the 
# class is being initiated.

class Student:
    # default constructors
    def __init__(self): #dunder method which isautomatically called
        pass
    # parameterized constructors
    def __init__(self, name, marks): 
        self.name = name
        self.marks = marks
        print("Adding a new student in database..")

s1 = Student("Sahil", 97)
print(s1.name, s1.marks)
s2 = Student("Yash", 88)
print(s2.name, s2.marks)


# *The "self" parameter is a reference to the current
# instance of the class, and is used to access variables