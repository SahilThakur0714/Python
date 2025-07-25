# Create student class that takes name & marks of 3 subjects as arguments 
# in constructor.
# Then create a method to print the average.

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def get_average(self):
        sum = 0
        for value in self.marks:
            sum += value
        print("hi", self.name, "your average is: ", sum/len(self.marks))


s1 = Student("Sahil", [99,98,97,96,95])
s1.get_average()

s1.name = "Tony Stark"
s1.get_average()