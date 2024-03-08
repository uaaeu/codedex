import random

print("=================================\nWelcome to Rock, Paper, Scissors!\n=================================")
print("Please choose one of the following options:")
print("1. ✊")
print("2. ✋")
print("3. ✌️")
player_choice = int(input("Enter your choice: "))
computer_choice = random.randint(1, 3)
if player_choice == 1 and computer_choice == 1:
    print("You chose: ✊")
    print("Computer chose: ✊")
    print("It's a tie!")
elif player_choice == 2 and computer_choice == 2:
    print("You chose: ✋")
    print("Computer chose: ✋")
    print("It's a tie!")
elif player_choice == 3 and computer_choice == 3:
    print("You chose: ✌️")
    print("Computer chose: ✌️")
    print("It's a tie!")
elif player_choice == 1 and computer_choice == 3:
    print("You chose: ✊")
    print("Computer chose: ✌️")
    print("You win!")
elif player_choice == 1 and computer_choice == 2:
    print("You chose: ✊")
    print("Computer chose: ✋")
    print("You lose!")
elif player_choice == 2 and computer_choice == 1:
    print("You chose: ✋")
    print("Computer chose: ✊")
    print("You win!")
elif player_choice == 2 and computer_choice == 3:
    print("You chose: ✋")
    print("Computer chose: ✌️")
    print("You lose!")
elif player_choice == 3 and computer_choice == 2:
    print("You chose: ✌️")
    print("Computer chose: ✋")
    print("You win!")
elif player_choice == 3 and computer_choice == 1:
    print("You chose: ✌️")
    print("Computer chose: ✊")
    print("You lose!")
else:
    print("Invalid choice! Please try again.")