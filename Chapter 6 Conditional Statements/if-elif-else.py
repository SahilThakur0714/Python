light = "pink"

if (light == "red"): #it always check the condition
    print("Stop the vehicle.")
elif(light == "green"): # it only checks if the 'if' conditon is false
    print("go")
elif(light == "yellow"):
    print("Look")
else: # if all the above conditions are false then 'else' execute
    print("Light is broken")

num = 5

if num > 2:
    print("greater than 2")
if num > 3:
    print("greater than 3")
elif num > 4:
    print("greater than the 4")