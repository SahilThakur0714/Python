# Deleting a File
# using the os module
# Module (like a code library) is a file written by another programmer 
# that generally has a functions we can use.

# import os
# os.remove( filename )

with open("demo.txt", "r") as f:
    data = f.read()
    print(data)


with open("demo.txt", "w") as f:
    f.write("new data")

import os
os.remove("sample.txt")