# Methods are functions that belong to objects
'''
Creating Class                              creating object
                                        
class Student:                              s1 = Student("Sahil")
def --init--(self,fullname):                s1.hello()
self.name = fullname

def hello(self):
    print("hello"),self.name

'''

class Student:
    college_name = "ABC College"
    def __init__(self, name, marks): 
        self.name = name
        self.marks = marks
        
    def welcome(self):
        print("Welcome", self.name)

    def get_marks(self):
        return self.marks

s1 = Student("Sahil", 97)
# print(s1.name, s1.marks)
s1.welcome()
print(s1.get_marks())