
# Repeat program 4 for a list of such words to be censored.

words = ["Donkey","ganda","rand","hai"]
with open(r"C:\Users\sahil\Desktop\Python\Chapter 9 -PS\prob5.txt","r") as f:
    content = f.read()
    for word in words:
        content =  content.replace(word,"#"*len(word))
    
with open(r"C:\Users\sahil\Desktop\Python\Chapter 9 -PS\prob5.txt","w") as f:
    f.write(content)