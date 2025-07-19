# Write a program to store seven fruits in a list entered by the user.
fruits = []
fruits.append(input("Enter fruit1: "))
fruits.append(input("Enter fruit2: "))
fruits.append(input("Enter fruit3: "))
fruits.append(input("Enter fruit4: "))
fruits.append(input("Enter fruit5: "))
fruits.append(input("Enter fruit6: "))
fruits.append(input("Enter fruit7: "))

print(fruits)


# Write a program to accept marks of 6 students and display them in a sorted
# manner.

marks = []
stu1 = int(input("Enter your marks:"))
marks.append(stu1)
stu2 = int(input("Enter your marks:"))
marks.append(stu2)
stu3 = int(input("Enter your marks:"))
marks.append(stu3)
stu4 = int(input("Enter your marks:"))
marks.append(stu4)
stu5 = int(input("Enter your marks:"))
marks.append(stu5)
stu6 = int(input("Enter your marks:"))
marks.append(stu6)

marks.sort()
print(marks)




# Check that a tuple type cannot be changed in python.
# a = (34, "Harry")
# a[2] = "Larry"
# we cannot do it