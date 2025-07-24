# From a file containing numbers separated by comma, print the count 
# of even numbers.
count = 0
with open(r"C:\Users\sahil\Desktop\Python\Chapter 9 -PS\practice3.txt", "r") as f:
    data = f.read()
    print(data)
        
    nums = data.split(",")   
    for value in nums:
        if(int(value)%2==0):
            count += 1
        
print(count)      
        
        # OR

    # num = ""
    # for i in range(len(data)):
    #     if(data[i] == ","):
    #         print(int(num))
    #         num = ""
    #     else:
    #         num += data[i]