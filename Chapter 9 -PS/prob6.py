# Write a program to mine a log file and find out whether it contains 'python'.
with open(r"C:\Users\sahil\Desktop\Python\Chapter 9 -PS\prob6.txt") as f:
    lines = f.read()

line_no = 1
for line in lines:
    if("python" in lines):
        line_no += 1
print("Yes it is present")
print(line_no)
      
# else:
#     print("not present")
        