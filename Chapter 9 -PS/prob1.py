# Write a program to read the text from a given file 'poems.txt' and 
# find out whether it contains the word 'twinkle'.
def check_for_word():
    with open(r"C:\Users\sahil\Desktop\Python\Chapter 9 -PS\peom.txt","r") as f:
        poem = f.read()

        # if(poem.find("twinkle") != -1):
        #     print("Found")
        # Or
        if("twinkle" in poem):
            print("Found")

        else:
            print("not Found")
    

check_for_word()


