# Multi level inheritance

class Car:
    
    @staticmethod
    def start():
        print("Car started...")

    @staticmethod
    def stop():
        print("Car stoped...")
        return 

class Toyota(Car):
    def __init__(self, brand):
        self.brand = brand


class Fortuner(Toyota):
    def __init__(self, type):
        self.brand = type

car1 = Fortuner("diesel")
car1.start()

# Multiple Inheritance
 
class A:
    varaA = "welcome to class A"

class B:
    varaB = "welcome to class B"
class C(A,B):
    varaC = "welcome to class C"

c1 = C()
print(c1.varaA,c1.varaB,c1.varaC,sep="\n")