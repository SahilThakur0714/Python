# with syntax 
# with open("demo.txt",a) as f:
    # data = f.read()

with open("demo.txt", "r") as f:
    data = f.read()
    print(data)


with open("demo.txt", "w") as f:
    f.write("new data")