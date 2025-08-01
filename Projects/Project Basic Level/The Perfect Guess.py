# # We are going to write a program that generates a random number and asks 
# # the user to guess it.
# # If the player's guess is higher than the actual number, the program 
# # 'displays "Lower number please". Similarly, if the user's guess is too 
# # low, the program prints "higher number please" When the user guesses 
# # the correct number, the program displays the number of guesses the 
# # player used to arrive at the number.
# # Hint: Use the random module.

# import random

# def guess():
#     r = random.randint(1,100)
#     a = -1
#     guess_no = 0
#     while (a != r):
#         n = int(input("Guess the number: "))
#         guess_no += 1
#         if(n == r):
#             # #guess_no += 1
#             print(f"You guessed it! the number is {n}")
#             print(f"You guess the number right in {guess_no} guesses")
#             break
#         elif(n < r):
#             print("Higher number please")
#             # guess_no += 1
#             # n = int(input("Guess the number: "))
        
#         # elif(n > r):
#         else:
#              print("Lower number please")
#             #  guess_no += 1
#             #  n = int(input("Guess the number: "))

# guess()



#    More correct and optimised

import random
n = random.randint(1,100)
a = -1
guesses = 0
while True and (guesses < 10):
    a = int(input("Guess the number: "))
    guesses += 1
    if(n == a):
            print(f"You guessed it! the number is {n}")
            break
    elif(a > n):
        print("Lower number please")

    elif(a < n):
        print("Higher number please")
        

print(f"You guessed the number {n} correctly in {guesses} guesses")

