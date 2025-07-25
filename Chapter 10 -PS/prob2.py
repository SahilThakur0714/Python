# Write a class "calculator" capable of finding square, cube and square 
# root of a number.

class Calculator:
    def __init__(self,n):
        self.n = n

    def get_square(self):
        print(f"Square is {self.n**2}")

    def get_cube(self):
        print(f"CUbe is {self.n**3}")
      
    def get_squareRoot(self):
        print(f"Square root is {self.n**1/2}")

c1 = Calculator(4)
c1.get_square()
c1.get_cube()
c1.get_squareRoot()