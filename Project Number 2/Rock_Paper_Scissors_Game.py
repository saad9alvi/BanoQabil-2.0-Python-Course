# Rock, Paper, Scissors Game
# Author: [Areeb Alvi]
# Roll Number: [06]
# Email: [saad9alvi@gmail.com]

# Problem Statement:
# Create a simple Rock, Paper, Scissors game where the user can play against the computer.
# The game should continue until the user decides to quit by typing 'Q'.

import random

# Initialize variables to track user and computer wins
user_wins = 0
computer_wins = 0

# Define the options for the game
options = ["rock", "paper", "scissors"]

# Main game loop
while True:
    # Get user input
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()

    # Check if the user wants to quit
    if user_input == "q":
        break

    # Check if the user input is valid
    if user_input not in options:
        print("Invalid input. Please choose Rock, Paper, or Scissors.")
        continue

    # Generate a random choice for the computer
    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    # Determine the winner and update the scores
    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
    elif user_input == computer_pick:
        print("Tied!")
    else:
        print("You lost!")
        computer_wins += 1

# Display the final results
print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Thanks For Playing!")
