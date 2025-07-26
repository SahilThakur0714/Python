# Create a class 'Employee' and add salary and increment properties to it.
# Write a method 'salaryAfterlncrement' method with a @property decorator 
# with a setter which changes the value of increment based on the salary.

class Employee:
    def __init__(self, salary, increment):
        self.salary    = salary
        self.increment = increment

    @property
    def salaryAfterIncrement(self):
        return (f" {self.salary + self.salary*(self.increment/100)}")

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary/self.salary) - 1) * 100

e = Employee(500,600)
print(e.salaryAfterIncrement)
e.salaryAfterIncrement = 280.9
print(e.salaryAfterIncrement)