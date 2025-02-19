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
=========''', 
'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
#Word bank of animals
word_list = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

#word_list = ["aardvak", "baboon", "camel"]

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

#Ask the user to guess and again & again. and check for the user lives, those will be start from 6 and end with 0
lives = 6
game_over = False
correct_letters = []
while not game_over:
    display = ""   
    guess_letter = input("Guess a letter:")
    for letter in chosen_word:        
        if letter == guess_letter:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
           
        
    print(display)
    if guess_letter not in chosen_word:
        lives -= 1
        #print(lives)
        if lives == 0 :
            game_over = True
            print('you lose!')
  
    

    if "_" not in display:
        game_over = True
        print("You Win!!")

    print(stages[-(lives+1)])

