import random


def game():
    number_of_rounds = 3
    current_round = 0
    print("You are playing rock, paper, scissors")
    while current_round < number_of_rounds:
        players_choice = input("Please type R for rock, P for paper and S for scissors").strip().upper()
        players_input_dict = {"R": "rock", "P": "paper", "S": "scissors"}
        computers_input_dict = {0: "rock", 1: "paper", 2: "scissors"}
        player = players_input_dict[players_choice]

        random_number = random.randint(0, 2)
        computer = computers_input_dict[random_number]
        print(f"You chose {player} and computer chose {computer}")

        if player == computer:
            print("It's a tie, choose again.")
            continue
        elif player == "rock":
            if computer == "scissors":
                print("You won!")
            else:
                print("You lost!")
        elif player == "scissors":
            if computer == "paper":
                print("You won!")
            else:
                print("You lost!")
        elif player == "paper":
            if computer == "rock":
                print("You won!")
            else:
                print("You lost!")
        current_round += 1


game()
