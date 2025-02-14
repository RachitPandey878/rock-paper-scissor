import random

# making the options
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

# determine the winner
def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    
    if (player == "rock" and computer == "scissors") or \
       (player == "scissors" and computer == "paper") or \
        (player == "paper" and computer == "rock"): 
        return "You win!"
    
    return "Computer wins!"

