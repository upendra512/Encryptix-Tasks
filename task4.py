# ROCK-PAPER-SCISSORS GAME
import tkinter as tk
from tkinter import messagebox
import random

# Initialize scores
user_score = 0
computer_score = 0

# Function to determine the winner
def determine_winner(user_choice):
    global user_score, computer_score
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)
    
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper') or \
         (user_choice == 'Paper' and computer_choice == 'Rock'):
        result = "You win!"
        user_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1
    
    result_label.config(text=f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n{result}")
    score_label.config(text=f"User Score: {user_score} | Computer Score: {computer_score}")

# Function to handle the user's choice
def user_choice(choice):
    determine_winner(choice)

# Function to ask if the user wants to play again
def play_again():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="")
    score_label.config(text="User Score: 0 | Computer Score: 0")

# Main window
root = tk.Tk()
root.title("Rock-Paper-Scissors")

# Instructions
tk.Label(root, text="Choose Rock, Paper, or Scissors:").pack()

# Buttons for user choices
tk.Button(root, text="Rock", command=lambda: user_choice('Rock')).pack()
tk.Button(root, text="Paper", command=lambda: user_choice('Paper')).pack()
tk.Button(root, text="Scissors", command=lambda: user_choice('Scissors')).pack()

# Label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

# Label to display the score
score_label = tk.Label(root, text="User Score: 0 | Computer Score: 0")
score_label.pack()

# Play again button
tk.Button(root, text="Play Again", command=play_again).pack()

root.mainloop()

