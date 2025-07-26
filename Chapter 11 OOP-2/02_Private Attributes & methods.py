# Conceptual Implementations in Python
# Private attributes & methods are meant to be used only within the class 
# and are not accessible from outside the class.

class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no   = acc_no
        self.__acc_pass = acc_pass
    def reset_pass(self):
        print(self.__acc_pass)


acc1 = Account("1234","abcd")
print(acc1.acc_no)
# print(acc1.acc_pass) #this is a worng practice
print(acc1.reset_pass())

# Correct way
class Person:
    def __hello(self):
        print("hello Boss")

    def welcome(self):
        self.__hello()

p1 = Person()
print(p1.welcome())