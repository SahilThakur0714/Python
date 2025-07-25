# Create a Class "Programmer" for storing information of few programmers
# working at Microsoft.

class Programmer:
    company = "Microsoft"

    def __init__(self,name,sal,pin):
        self.name   = f"name: {name}"
        self.pin    = f"pincode: {pin} "
        self.salary = f"salary: {sal}"
        

e1 = Programmer("Sahil Thakur",444207 ,1000000 )
print(e1.name,e1.pin,e1.salary,e1.company,sep="\n")