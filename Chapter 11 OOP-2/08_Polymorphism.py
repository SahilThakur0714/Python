# Operator Overloading: When the same operator is allowed to have 
# different meaning according to the context.

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img  = img

    def show_Number(self):
        print(f"({self.real})i + ({self.img})j")

    def __add__(self,num):
        new_Real = self.real + num.real
        new_Img  = self.img  + num.img
        return Complex(new_Real, new_Img)

    def __sub__(self,num):
        new_Real = self.real - num.real
        new_Img  = self.img  - num.img
        return Complex(new_Real, new_Img)

num1 = Complex(1, 3)
num1.show_Number()

num2 = Complex(4, 6)
num2.show_Number()

num3 = num1 + num2
num3.show_Number()

num4 = num1 - num2
num4.show_Number()