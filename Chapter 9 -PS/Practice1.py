''' 
Create a new file "practice.txt" using python. Add the following data in it:
Hi everyone
we are learning File 1/0
using Java.
I like programming in Java.


'''
# WAF that replace all occurrences of "java" with "python" in above file.

# with open(r"C:\Users\sahil\Desktop\Python\Chapter 9 -PS\practice.txt","w") as f:
    # f.write("Hi everyone \nwe are learning File I/O\n")
    # f.write("using Java.\nI like programming in Java.")



# with open(r"C:\Users\sahil\Desktop\Python\Chapter 9 -PS\practice.txt","r") as f:
#     data = f.read()

# new_data = data.replace("Java", "Python")
# print(new_data)


# with open(r"C:\Users\sahil\Desktop\Python\Chapter 9 -PS\practice.txt","w") as f:
#      f.write(new_data)




# Search if the word "learning" exists in the file or not.

def check_for_word():

    with open(r"C:\Users\sahil\Desktop\Python\Chapter 9 -PS\practice.txt","r") as f:
        data = f.read()

        if (data.find("learning") != -1):
            print("found")
        else:
            print("not found")

check_for_word()

