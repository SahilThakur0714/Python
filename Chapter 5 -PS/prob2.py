# Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value end use key as their names. Assume that the names are unique.

d= {}

name = input("enter friends name: ")
lang = input("enter language name: ")

d.update({name: lang})
name = input("enter friends name: ")
lang = input("enter language name: ")

d.update({name: lang})
name = input("enter friends name: ")
lang = input("enter language name: ")

d.update({name: lang})
name = input("enter friends name: ")
lang = input("enter language name: ")

d.update({name: lang})

print(d)
