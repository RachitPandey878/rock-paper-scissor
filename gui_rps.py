import tkinter as tk
import random
import game_logic

player_score = 0
computer_score = 0

def play(choice):

    global player_score, computer_score

    computer_choice = game_logic.get_computer_choice()

    result = game_logic.determine_winner(choice, computer_choice)

    if result == "You win!":
        player_score += 1   
    elif result == "Computer wins!":
        computer_score += 1

    player_Label.config(text=f"Your Choice: {choice}")
    computer_Label.config(text=f"Computer Choice: {computer_choice}")
    result_Label.config(text=result)
    score_Label.config(text=f"Score: You {player_score} - {computer_score} Computer")

def reset_game():
    global player_score, computer_score
    player_score = 0
    computer_score = 0
    score_Label.config(text="Score: You 0 - 0 Computer")
    result_Label.config(text="")


root = tk.Tk()
root.title("Rock, Paper, Scissors - GUI Version")

player_Label = tk.Label(root, text="Your Choice: ",font=("Arial",14))
player_Label.pack()

computer_Label = tk.Label(root, text="Computer Choice: ",font=("Arial",14))
computer_Label.pack()

result_Label = tk.Label(root, text="",font=("Arial",14))
result_Label.pack()

score_Label = tk.Label(root, text="Score: You 0 - 0 Computer",font=("Arial",14))
score_Label.pack()

rock_button = tk.Button(root, text="Rock", command=lambda: play("rock"))
rock_button.pack(side=tk.LEFT, padx=10)

paper_button = tk.Button(root, text="Paper", command=lambda: play("paper"))
paper_button.pack(side=tk.LEFT, padx=10)

scissors_button = tk.Button(root, text="Scissors", command=lambda: play("scissors"))
scissors_button.pack(side=tk.LEFT, padx=10)

reset_button = tk.Button(root, text="Reset", font=("Arial", 14), command=reset_game)
reset_button.pack(side=tk.LEFT, padx=10)

root.mainloop()