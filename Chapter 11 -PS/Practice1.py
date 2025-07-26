# Define a Circle class to create a circle with radius r using the 
# constructor.Define an Area() method of the class which calculates the 
# area of the circle.Define a Perimeter() method of the class which allows
#  you to calculate the perimeter of the circle.
from math import pi
class Circle:
    def __init__(self,r):
        self.r = r

    def area(self):
        return f"{pi*(self.r**2):.2f}"
    
    def perimeter(self):
        return f"{2*pi*self.r:.2f}"
    
x1 = Circle(21)
print(x1.area())
print(x1.perimeter())

# Qs. Define a Employee class with attributes role, department & salary. 
# This class also has a showDetaiIs( ) method.
# Create an Engineer class that inherits properties from Employee & has 
# additional attributes : name & age.

class Employee:
    def __init__(self,role,department,salary):
        self.role       = role
        self.department = department
        self.salary     = salary

    def showDetails(self):
        print("role =",self.role)
        print("depatment =",self.department)
        print("salary =",self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age  = age
        super().__init__("Engineer","IT","75000")

engg1 = Engineer("Tony Stark", 40)
engg1.showDetails()