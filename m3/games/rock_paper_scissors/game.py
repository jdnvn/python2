import random

options = ['rock', 'paper', 'scissors']
user_input = None
while user_input is None:
    user_input = input(f"Choose {", ".join(options)}\n")
    user_choice = user_input.lower()
    if user_choice not in options:
        print("Invalid choice!")
        user_input = None

computer_choice = random.choice(options)

print("computer chooses", computer_choice)

if user_choice == computer_choice:
    print("Tie")
elif user_choice == 'paper':
    if computer_choice == 'rock':
        print("You win!")
    elif computer_choice == 'scissors':
        print("You lose :(")
elif user_choice == 'rock':
    if computer_choice == 'paper':
        print("You lose :(")
    elif computer_choice == 'scissors':
        print("You win!")
elif user_choice == 'scissors':
    if computer_choice == 'rock':
        print("You lose :(")
    elif computer_choice == 'paper':
        print("You win!")
else:
    raise Exception(f"Invalid choice: {user_choice}")
