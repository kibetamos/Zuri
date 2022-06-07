from ast import Continue
import random

user_action = input("Enter a choice (R, P, S): ")
possible_actions = ["R", "P", "S"]
while user_action not in possible_actions:
    print("Wrong Answer")
    user_action = input("Enter a choice (R, P, S): ")

computer_action = random.choice(possible_actions)
print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")



while user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")
    user_action = input("Enter a choice (R, P, S): ")


if user_action == "R":
    if computer_action == "S":
        print("R smashes S! You win!")
    else:
        print("P covers R! You lose.")
elif user_action == "P":
    if computer_action == "R":
        print("P covers R! You win!")
    else:
        print("S cuts P! You lose.")
elif user_action == "S":
    if computer_action == "P":
        print("S cuts P! You win!")
    else:
        print("R smashes S! You lose.")