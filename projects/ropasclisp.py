from random import randint
import os

# create a list of play options
s = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

computer = s[randint(0,4)]

# set player to 'False'
player = False

while player == False:
    os.system('cls') # hat Robin geschrieben, 'cleared' das Terminal nach einmaliger Ausführung
    player = input("Choose wisely: Rock, Paper, Scissors, Lizard or Spock?\n > ")
    print(f"Player: {player}\nComputer: {computer}")
    if player == computer:
        print("It's a draw! Try again.")
    elif player == "Rock":                                       
        if computer == "Paper":
            print(f"You lost! {computer} covers {player}")
        elif computer == "Scissors":
            print(f"You won! {player} smashes {computer}")
        elif computer == "Lizard":
            print(f"You won! {player} crushes {computer}")
        else:
            print(f"You lost! {computer} vaporizes {player}")
    elif player == "Paper":
        if computer == "Scissors":
            print(f"You lost! {computer} cuts {player}")
        elif computer == "Rock":
            print(f"You won! {player} covers {computer}")
        elif computer == "Lizard":
            print(f"You lost! {computer} eats {player}")
        else:
            print(f"You won! {player} disproves {computer}")
    elif player == "Scissors":
        if computer == "Rock":
            print(f"You lost! {computer} smashes {player}")
        elif computer == "Paper":
            print(f"You won! {player} cuts {computer}")
        elif computer == "Lizard":
            print(f"You won! {player} decapitates {computer}")
        else:
            print(f"You lost! {computer} smashes {player}")
    elif player == "Lizard":
        if computer == "Rock":
            print(f"You lost! {computer} smashes {player}")
        elif computer == "Paper":
            print(f"You won! {player} eats {computer}")
        elif computer == "Scissors":
            print(f"You lost! {computer} decapitates {player}")
        else:
            print(f"You won! {player} poisons {computer}")
    elif player == "Spock":
        if computer == "Rock":
            print(f"You won! {player} vaporizes {computer}")
        elif computer == "Paper":
            print(f"You lost! {computer} disproves {player}")
        elif computer == "Lizard":
            print(f"You lost! {computer} poisons {player}")
        else:
            print(f"You won! {player} smashes {computer}")
    else:
        print("This is not a valid option. Check your spelling!")
    input("Press Enter to continue.")


    
    player = False
    computer = s[randint(0, 4)]