# Python can be used to perform operations on a file. (read & write data)
# Types of all files
# 1 . Text Files : .txt, .docx, .10g etc.
# 2. Binary Files : .mp4, .mov, .png, .jpeg etc.

# The random-access memory is volatile, and all its contents are lost once 
# a program terminates in order to persist the data forever, we use files.
# A file is data stored in a storage device. A python program can talk to 
# the file by reading content from it and writing content to it.

# syntax: f = open("file_name", "mode")

# f = open(r"C:\Users\sahil\Desktop\Python\Chapter 9 Files\demo.txt", "r")
f = open("demo.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()


