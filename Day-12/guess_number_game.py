import art
import random
print(art.logo)
print("Welcome to the Number Guess game.!")
print("I'm thinking the number between 1 and 100")
difficulty = input("Choose difficulty. Type 'easy' or 'hard': ").lower()

computer_guess_number = random.choice(range(1,101))

if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5
else:
    print("Wrong difficulty!. Enter 'easy' or 'hard' for difficulty")

def guess_number():
    global attempts
    is_guess_correct = False    
    while not is_guess_correct:
        if attempts > 0:
            print(f"You have {attempts} attempts remaining to guess the number.")
            num = int(input("Make a guess: "))
            if num > computer_guess_number:
                print("Too High")
                print("Guess again!")
                attempts -= 1
            if num < computer_guess_number:
                print("Too Low")
                print("Guess again!")
                attempts -= 1
            if num == computer_guess_number:
                print(f"Your got it!. The answer was {computer_guess_number}")
                is_guess_correct = True
        else:
            print(f"You run out of guesses!. The answer was {computer_guess_number}")
            break

guess_number()