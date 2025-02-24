# importing random
import random


# defining a function
def game():
    # setting the number of round to 3
    number_of_rounds = 3
    # initialising a variable current round set to 0
    current_round = 0
    # printing a statement for context
    print("You are playing rock, paper, scissors")

    # this while loop will exit due to continue if the round is a tie, allowing to replay
    while current_round < number_of_rounds:
        # taking an input from a participant, and removing spaces and capitilising with strip() and upper() methods
        players_choice = input("Please type R for rock, P for paper and S for scissors: ").strip().upper()
        # a dictionary for players input
        players_input_dict = {"R": "rock", "P": "paper", "S": "scissors"}
        # a dictionary for computer input
        computers_input_dict = {0: "rock", 1: "paper", 2: "scissors"}
        # getting a value for the players input from a the players input dictionary
        player = players_input_dict[players_choice]
        # generating a random number from 0 to 2
        random_number = random.randint(0, 2)
        # getting computer input value from the computer input dictionary
        computer = computers_input_dict[random_number]
        # printing what both players chose with an f string
        print(f"You chose {player} and computer chose {computer}")
        # this if statement will exit the while loop if it is a tie and print a corresponding statement
        if player == computer:
            print("It's a tie, choose again.")
            continue
        # this statement specifies all the cases where the player beats the computer and prints "You win!"
        elif (player == 'rock' and computer == 'scissors') or (player == 'paper' and computer == 'rock') or (
                player == 'scissors' and computer == 'paper'):
            print("You win!")
        # if none of the above are true, the player has lost, and it is printed
        else:
            print("You lose!")

        # this appends the current_round variable at the end of each completed round
        current_round += 1

# calling the function
game()
