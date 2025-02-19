import random
stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word_list = ["aardvak", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

# Create a "Placeholder" for each character in chosen word
placeholder = ""
for position in range(len(chosen_word)):
    placeholder += "_"

print(placeholder)

'''
#Ask the user to guess the letter
guess_letter=input("Guess a letter:").lower()

#Create display to put the guess letter in right position and _ in wrong position
display = ""
for letter in chosen_word:
    if letter == guess_letter:
        display += letter
    else:
        display += "_"

print(display)
'''

#Ask the user to guess and again & again.

game_over = False
correct_letters = []
while not game_over:
    display = ""
    guess_letter = input("Guess a letter:")
    for letter in chosen_word:        
        if letter == guess_letter:
            display += letter
            correct_letters.append(guess_letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    if "_" not in display:
     game_over = True
     print("You Win!!")






           
    


    





