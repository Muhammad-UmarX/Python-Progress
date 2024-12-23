import random

choices = ["Rock", "Paper", "Scissors"]
user_choice = (input("Enter your choice: ")).upper()
computer_choice = (random.choice(choices)).upper()

if user_choice == computer_choice:
    print("It's a draw")
    print(f"You: {user_choice} | Computer: {computer_choice}")
elif (user_choice == "ROCK" and computer_choice == "SCISSORS") or (user_choice == "PAPER" and computer_choice == "ROCK") or (user_choice == "SCISSORS" and computer_choice == "PAPER"):
    print("You Win")
    print(f"You: {user_choice} | Computer: {computer_choice}")
elif (user_choice == "ROCK" and computer_choice == "PAPER") or (user_choice == "PAPER" and computer_choice == "SCISSORS") or (user_choice == "SCISSORS" and computer_choice == "ROCK"):
    print("Computer Wins!")
    print(f"You: {user_choice} | Computer: {computer_choice}")
else:
    print("Invalid Choice")

