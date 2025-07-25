# Add a static method in problem 2, to greet the user with hello.

class Calculator:
    def __init__(self,n):
        self.n = n
    
    @staticmethod
    def greet():
        print("Hello")

    def get_square(self):
        print(f"Square is {self.n**2}")

    def get_cube(self):
        print(f"CUbe is {self.n**3}")
      
    def get_squareRoot(self):
        print(f"Square root is {self.n**1/2}")

c1 = Calculator(4)
c1.greet()
c1.get_square()
c1.get_cube()
c1.get_squareRoot()