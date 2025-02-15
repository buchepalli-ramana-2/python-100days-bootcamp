# Playing Rock scissor paper game with computer.
# Here is the reference game https://wrpsa.com/

import random

rock = "✊"
paper = "✋"
scissor = "✂"

game_choices = [rock, paper, scissor]

computer_choice = random.randint(0,2)

user_choice = int(input("Which option you will choose. 0 for rock, 1 for paper, 2 for scissor "))

if user_choice >= 0 and user_choice <3:
    print(game_choices[user_choice])
    print(game_choices[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You Win!!")
    elif user_choice == 2 and computer_choice == 0:
        print("You Lose!!")
    elif user_choice > computer_choice:
        print("You Win!!")
    elif user_choice < computer_choice:
        print("You Lose!")
    elif user_choice == computer_choice:
        print("It's draw!!")
else:
    #user_choice < 0 and user_choice >= 3:
    print("Invalid choice, You Lose!")



