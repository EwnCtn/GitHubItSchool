import random

while True: 
    print('')
    print(" --- Welcome to the rock/paper/scissors game: --- ")
    print('')
    option = ["rock", "paper", "scissors"] 

    computer = random.choice(option)
    player = None

    while player not in option:
       player = input("rock, paper or scissors: ").lower()

    if player == computer:
        print("computer: ", computer)
        print("player: ",player)
        print("Tie !")

    elif player == "rock":
        if computer == "paper":
            print("computer: ", computer)
            print("player: ",player)
            print("You lose !")
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ",player)
            print("You win !")
    elif player == "paper":
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ",player)
            print("You lose !")
        if computer == "rock":
            print("computer: ", computer)
            print("player: ",player)
            print("You win !")
    elif player == "scissors":
        if computer == "rock":
            print("computer: ", computer)
            print("player: ",player)
            print("You lose !")
        if computer == "paper":
            print("computer: ", computer)
            print("player: ",player)
            print("You win !")
    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break

print('ok bisou bye')