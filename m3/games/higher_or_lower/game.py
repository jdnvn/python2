import random

print("Welcome to Higher or Lower! Choose a number between 1 and 100")
answer = random.randint(1, 100)

while True:
    user_input = input("Choose a number: ")
    try:
        choice = int(user_input)

        if choice == answer:
            print("YOU GUESSED THE NUMBER!")
            break
        elif choice > answer:
            print(f"{choice} is higher than my number")
        else:
            print(f"{choice} is lower than my number")
    except ValueError:
        print("I'm sorry, but cheaters are not allowed. This is a noncheating game!!!!!")
        break
