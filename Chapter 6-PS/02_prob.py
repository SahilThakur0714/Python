# Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.

math_marks = int(input("Enter your marks in Maths: "))
code_marks = int(input("Enter your marks in Coding: "))
science_marks = int(input("Enter your marks in Science: "))

math_pass = (math_marks/100)*100
code_pass = (code_marks/100)*100
science_pass = (science_marks/100)*100
result = ((math_marks + science_marks + code_marks)/300)*100

if(math_pass < 33):
    print("\nFailed in Maths")
else:
    print("\nPassed in Maths")
print(f"Maths Score = {round(math_pass, 2)}%")

if(code_pass< 33):
    print("\nFailed in Coding")
else:
    print("\nPassed in Coding")
print(f"Coding Score = {round(code_pass, 2)}%")

if(science_pass < 33):
    print("\nFailed in Science")
else:
    print("\nPassed in Science")
print(f"Science Score = {round(science_pass, 2)}%")

print(f"\nOverall score = {round(result, 2)}%")
if not (result >= 40 and math_pass >= 33 and science_pass >= 33 and code_pass >= 33 ):
    print("Result: Failed")
else:
    print("Result: Passed")
