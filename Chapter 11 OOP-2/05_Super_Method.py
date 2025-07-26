# Super Method: is used to access methods of parents class

class Car:
    
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car started...")

    @staticmethod
    def stop():
        print("Car stoped...")
        return 

class Toyota(Car):
    def __init__(self, name,type):
        super().__init__(type)
        self.brand = name
        super().start()

car1 = Toyota("Prius","electirc")
print(car1.type)