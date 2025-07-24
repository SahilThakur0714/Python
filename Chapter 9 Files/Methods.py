'''
Character                               Meaning

'r'                 open for reading (default)
'w'                 open for writing, truncating the file first
'x'                 create a new file and open it for writing
'a'                 open for writing, appending to the end of the file if it exists
'b'                 binary mode
't'                 text mode (default)
'+'                 open a disk file for updating (reading and writing)

'''

# f = open("demo.txt","r")
# data = f.read(5)
# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)

# f.close()


f = open("demo.txt","r+")
f.write("abc")
print(f.read())
f.close()