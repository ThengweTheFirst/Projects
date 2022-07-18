"""
Problem: Trying your luck
Target Users: Me and Everyone who can access the game
Target System: Windows, Linux, Unix, Mac OS
Interface: Command-line
Functional Requirements: Use python terminal to play the game
Testing: Simple test
"""
_version_ = 0.1

print("THENGWE")
print("proudly presents")
print("The NumGuesser")

# To know who's playing
playername = input("May you kindly type in your name: ")

print("Welcome " + playername + " to The Numguesser")

import random

max = input("Please type in a number: ")

# To check if the users input is an interger or actually a number.
if max.isdigit():
    max = int(max)

    if max <= 0:
        print("Please type in a number larger than 0 next time.")
        quit()
else:
    print("Please type in a number next time.")
    quit()


random_number = random.randint(0, max)
# To know how many tries or guesses before the user got it correct.
guesses = 0

while True:
    guesses += 1
    player_guess = input("Make a guess: ")
    # To check if the user typed in a number.
    if player_guess.isdigit():
        player_guess = int(player_guess)
    else:
        print("Please type in a number next time.")
        continue

    # To check if the guess is equal, greater or less than the random_number.
    if player_guess == random_number:
        print("Congratulations you guessed correctly.")
        break
    elif player_guess > random_number:
        print("Ooh that is above the number")
    else:
        print("You fall short.")

# To inform the user of his/her performance
print("You got it in ", guesses ," guesses")