# Static Methods
# Methods that don't use the self parameter (work at class level)


class Student:

    def __init__(self, name, marks): 
        self.name = name
        self.marks = marks

    @staticmethod  #decorator
    def hello(): 
        print("ABC college")

s1 = Student("sahil",91)
s1.hello()

# Decorator:*Decorators allow us to wrap another function in order to
# extend the behaviour of the wrapped function, without
# permanently modifying it