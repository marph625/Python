# import random integers from module 'random'
from random import randint

# create a list of play options
# also known as 'array' in other languages
s = ["Rock", "Paper", "Scissors"]

# computer chooses a random element from the list s with the elements [0 = "Rock", 1 = "Paper", 2 = "Scissors"]
computer = s[randint(0,2)]

# set player to 'False'
player = False

# while player is false the loop continues
while player == False:
    
    # While loop begins
    
    # Variable 'player' is assigned to a new value within the while loop
    # In this case: player = whatever we type in
    player = input("Choose wisely: Rock, Paper or Scissors?\n> ") 
    
    if player == computer:                                      # 1. First we ask if the player and the computer made the same choice
        print("It's a draw! Try again.")
    elif player == "Rock":                                      # We need to check all cases:
        if computer == "Paper":                                 # 2. Rock vs. Paper/Scissors
            print("You lost!", computer, "covers", player)
        else:
            print(f"You won! {player} smashes {computer}")      # f-String looks better
    elif player == "Paper":                                     # 3. Paper vs. Scissors/Rock
        if computer == "Scissors":
            print("You lost!", computer, "cuts", player)
        else:
            print("You won", player, "covers", computer)
    elif player == "Scissors":                                  # 4. Scissors vs. Rock/Paper
        if computer == "Rock":
            print("You lost!", computer, "smashes", player)
        else:
            print("You won!", player, "cuts", computer)
    else:                                                       # 5. If you type anything other than 'Rock', 'Paper' or 'Scissors' you're gonna get this message.
        print("This is not a valid option. Check your spelling!")
    
    player = False  # player was set to True, but we want it to be False so the loop continues 
    computer = s[randint(0, 2)] # computer makes another choice