import random
from collections import Counter

# Track player's move history
player_move_history = []

def get_computer_choice():
    """Chooses based on player's most frequent move, otherwise random."""
    if len(player_move_history) >= 3:
        # Count the most common move by the player
        move_counts = Counter(player_move_history)
        most_common_move = move_counts.most_common(1)[0][0]  # Get most used move

        # Choose the move that beats the player's most common move
        if most_common_move == "rock":
            return "paper"  # Paper beats rock
        elif most_common_move == "paper":
            return "scissors"  # Scissors beats paper
        elif most_common_move == "scissors":
            return "rock"  # Rock beats scissors
    
    # If not enough history, pick randomly
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player, computer):
    """Determines the winner based on player and computer choices."""
    if player == computer:
        return "It's a tie!"
    
    if (player == "rock" and computer == "scissors") or \
       (player == "scissors" and computer == "paper") or \
       (player == "paper" and computer == "rock"):
        return "You win!"
    
    return "Computer wins!"
