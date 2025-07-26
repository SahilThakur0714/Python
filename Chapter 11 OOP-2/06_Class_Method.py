# A class method is bound to the class & receives the class as an implicit first 
# argument.
# Note - static method can't access or modify class state & generally 
#            for utility.

class Person:
    name = "annonymous"
    @classmethod
    def changeName(self, name):
        self.name = name

p1 = Person()
p1.changeName("Yash")
# print(p1.name)
print(Person.name)

# or

class Person:
    name = "annonymous"
    
    def changeName(self, name):
        self.__class__.name = name

p1 = Person()
p1.changeName("Sahil")
print(p1.name)
print(Person.name)

# or

class Person:
    name = "annonymous"
    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("Kartik")
print(p1.name)
print(Person.name)