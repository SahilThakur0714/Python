# Inheritance: When one class(childlderived) derives the properties & 
# methods of another class(parentlbase).

# syntax: 
# class Car:
    # ...
# class Toyota(Car):
    # ...

class Car:
    color = "black"
    @staticmethod
    def start():
        print("Car started...")

    @staticmethod
    def stop():
        print("Car stoped...")
        return 

class Toyota(Car):
    def __init__(self, name):
        self.name = name

car1 = Toyota("Fortuner")
car2 = Toyota("Prius")
        
print(car1.start())
print(car1.stop())
print(car2.color)