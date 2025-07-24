# A file contains a word "Donkey" multiple times. You need to write a program which
# replace this word with ##### by updating the same file.

words = "Donkey"
with open(r"C:\Users\sahil\Desktop\Python\Chapter 9 -PS\prob4.txt","r") as f:
    words = f.read()
    words =  words.replace("Donkey","#####")
    
with open(r"C:\Users\sahil\Desktop\Python\Chapter 9 -PS\prob4.txt","w") as f:
    f.write(words)
    