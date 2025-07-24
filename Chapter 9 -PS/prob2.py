# The game() function in a program lets a user play a game and returns 
# the score as an integer. You need to read a filékHi-score.txt' which is 
# either blank or contains the previous Hi-score. You need to write a 
# program to update the Hi-score whenever the game() function breaks the 
# Hi-score.
import random

def game():
    print('your are playing a game')
    score = random.randint(1, 200)
    with open(r"C:\Users\sahil\Desktop\Python\Chapter 9 -PS\Hi-score.txt") as f:
        hiscore  = f.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
        
    print(f"Your score: {score}")
    if(score>hiscore):
        with open(r"C:\Users\sahil\Desktop\Python\Chapter 9 -PS\Hi-score.txt", "w") as f:
            f.write(str(f"High Score: {score}"))
    return score

game()

