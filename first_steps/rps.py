from random import randint

# create a list of play options
s = ["Rock", "Paper", "Scissors"]

computer = s[randint(0,2)]

# set player to 'False'
player = False

while player == False:
    player = input("Choose wisely: Rock, Paper or Scissors?")
    if player == computer:
        print("It's a draw! Try again.")
    elif player == "Rock":                                       
        if computer == "Paper":
            print("You lost!", computer, "covers", player)
        else:
            print("You won!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lost!", computer, "cuts", player)
        else:
            print("You won", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lost!", computer, "smashes", player)
        else:
            print("You won!", player, "cuts", computer)
    else:
        print("This is not a valid option. Check your spelling!")
    
    player = False
    computer = s[randint(0, 2)]