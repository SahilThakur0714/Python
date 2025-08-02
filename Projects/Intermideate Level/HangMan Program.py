# Hangman in Python

from wordlist import words
import random


#dictionary of key:()
hangman_art = {0:("   ",
                  "   ",
                  "   "),
               1:(" o ",
                  "   ",
                  "   "),
               2:(" o  ",
                  " |  ",
                  "   "),
               3:("  o  ",
                  " /|  ",
                  "   "),
               4:("  o ",
                  " /|\\ ",
                  "   "),
               5:("  o ",
                  " /|\\ ",
                  " / "),
               6:("  o ",
                  " /|\\ ",
                  " / \\ ")}

def display_man(wrong_gusses):
    print("**********")
    for line in hangman_art[wrong_gusses]:
        print(line)
    print("**********")
def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = [ch if not ch.isalpha() else "_" for ch in answer]
    wrong_gusses = 0
    gussed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_gusses)
        display_hint(hint)
        print("Guessed letters:", " ".join(sorted(gussed_letters)))
        guess = input("Enter a letter (of Bollywood Movie): ")

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter one alphabet letter.")
            continue

        guess = guess.lower()
        if guess in gussed_letters:
            print(f"{guess.upper()} is already guessed")
            continue

        gussed_letters.add(guess)

        if guess in answer.lower():
            for i, ch in enumerate(answer):
                if ch.lower() == guess:
                    hint[i] = ch
        else:
            wrong_gusses += 1

        if "_" not in hint:
            display_man(wrong_gusses)
            display_answer(answer)
            print("🎉 YOU WIN!")
            is_running = False

        elif wrong_gusses >= len(hangman_art) - 1:
            display_man(wrong_gusses)
            display_answer(answer)
            print("😢 YOU LOSE!")
            is_running = False


if __name__ == "__main__":
    main()