class Student:
    college_name = "ABC College"
    def __init__(self, name, marks): 
        self.name = name
        self.marks = marks
        print("Adding a new student in database..")

s1 = Student("Sahil", 97)
print(s1.name, s1.marks)
s2 = Student("Yash", 88)
print(s2.name, s2.marks)

print(s2.college_name)
# print(Student.college_name)