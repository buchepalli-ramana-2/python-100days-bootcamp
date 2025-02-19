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

#Ask the user to guess and again & again. and check for the user lives, those will be start from 6 and end with 0
lives = 6
game_over = False
correct_letters = []

while not game_over:

    print(f"********Your no.of Lives left: {lives}/6 **************")

    guess_letter = input("Guess a letter:").lower()
    if guess_letter in correct_letters:
        print(f"You've already guess {guess_letter}")
    
    display = ""

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
        print(f"You guessed {guess_letter}, that's not in the word. You lose a life.")


        if lives == 0 :
            game_over = True
            print(f"************** It was '{chosen_word}'. you lose!***********")
  
    

    if "_" not in display:
        game_over = True
        print(f"*******************You Win!**************")

    print(stages[-(lives+1)])

