# Write a program to create a dictionary of Hindi words with values
#  as their English
# translation. Provide user with an option to look it up!

hindi_Dictionary = {
    "samay": "time",
    "aatang": "terror",
    "amir": "rich",
    "sahil":"seashore"
}

word = input("Enter the words you want meaning of: ")
print(hindi_Dictionary.get(word))

# Write a program to input eight numbers from the user and display
#  all the unique numbers (once).

numbers = set()
x = (input("Enter a no: "))
numbers.add(int(x))
x = (input("Enter a no: "))
numbers.add(int(x))
x = (input("Enter a no: "))
numbers.add(int(x))
x = (input("Enter a no: "))
numbers.add(int(x))
x = (input("Enter a no: "))
numbers.add(int(x))
x = (input("Enter a no: "))
numbers.add(int(x))
x = (input("Enter a no: "))
numbers.add(int(x))
x = (input("Enter a no: "))
numbers.add(int(x))

print(numbers)
