import random

# making the options
def get_computer_choice():
    return random.choice["rock", "paper", "scissors"]

# determine the winner
def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    
    if (player == "rock" and computer == "scissors") or \
       (player == "scissors" and computer == "paper") or \
        (player == "paper" and computer == "rock"): 
        return "You win !"
    
    return "Computer wins !"


# make the game interactive

def main():
    print("Welcome to Rock, Paper, Scissors!")

    while True:
        
        player_choice = input("Choose rock, paper, or scissors (or 'quit' to exit):").lower()

        if player_choice == "quit":
            print("Thanks for playing!")
            break

        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice()
        print(f"computer_choice: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)
        print(result)
        print("-"*30)

if __name__ == "__main__":
    main()
    