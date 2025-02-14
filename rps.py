import game_logic

# make the game interactive

def main():
    print("Welcome to Rock, Paper, Scissors!")

    player_score = 0
    computer_score = 0

    while True:

        print(f"\nscore: You {player_score} - {computer_score} Computer")
        
        player_choice = input("Choose rock, paper, or scissors (or 'quit' to exit):").lower()

        if player_choice == "quit":
            print("\nFinal score:")
            print(f"you: {player_score} - Computer: {computer_score}")
            print("Thanks for playing!")
            break

        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = game_logic.get_computer_choice()
        print(f"computer choice: {computer_choice}")

        result = game_logic.determine_winner(player_choice, computer_choice)
        print(result)

        if result == "You win!":
            player_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        print("-"*30)

if __name__ == "__main__":
    main()
