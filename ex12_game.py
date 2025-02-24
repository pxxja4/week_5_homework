import random


def my_choice():
    choices = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}
    user_input = input("Enter R for Rock, P for Paper, S for scissors: ")
    return choices[user_input]
# print(my_choice())

def computer_option():
    choices = ['Rock', 'Paper', 'Scissors']
    return random.choice(choices)
# print(computer_option())

def winner(user,computer):
    if user == computer:
        return "It's a draw!"
    elif (user == 'Rock' and computer == 'Scissors') or \
            (user == 'Paper' and computer == 'Rock') or \
            (user == 'Scissors' and computer == 'Paper'):
        return "You win!"
    else:
        return "You lose!"


def play_game():
    user_choice = my_choice()
    computer_choice = computer_option()

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = winner(user_choice, computer_choice)
    print(result)
play_game()
