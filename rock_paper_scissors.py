# to allow the computers plays to be random.
import random

# defining the game.
def game():
    # Informing the player or user of the available options.
    print("'r' for rock, 'p' for paper, 's' for scissors")
    # Playtime
    print("What is your choice?")
    player = input()
    computer = random.choice(['r', 'p', 's'])
    #Determining if the player or user won.
    if player == computer:
        print("it's a tie") 
    elif is_win(player, computer):
        print("Congratulations you won!")
    else:
        print("You lose!")
# defining a win.
def is_win(player, computer):
    if (player == 'r' and computer == 's') or (player == 's' and computer == 'p') \
        or (player == 'p' and computer == 'r'):
        return

print(game())