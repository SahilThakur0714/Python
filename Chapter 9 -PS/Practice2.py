# WAF to find in which line of the file does the word "learning"occur 
# first.
# Print -1 if word not found.


def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open(r"C:\Users\sahil\Desktop\Python\Chapter 9 -PS\practice.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
            line_no += 1
            
    return -1    
    
check_for_line()