# Property: We use @property decorator on any method in the class to use 
# the method as a property

class Student:
    def __init__(self,phy,che,math):
        self.phy = phy
        self.che = che
        self.math = math
    @property
    def percentage(self):
        return str((self.phy + self.che + self.math) / 3) + "%"
    

stu1 = Student(98, 97, 99)
print(stu1.percentage)

stu1.phy = 86
print(stu1.percentage)