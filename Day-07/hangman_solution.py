word_list = ["aardvak", "baboon", "camel"]
#Todo choose a random word from the word list and assign to chosen word.
#Todo ask the user to guess a letter in the chosen word and assign it another variable. change to lowercase.
#Todo check the letter guessed by user is in chosen word then print "Right", "wrong" if it is not in the word.
import random
chosen_word = random.choice(word_list)
#print(chosen_word)

#for i in range(len(chosen_word)):
for i in range(5):
    guess_letter=input("Guess a letter:").lower()
    if guess_letter in chosen_word:
        if guess_letter == "":
            print("please enter one letter")
        else:
            print("Right")
    else:
        print("Wrong")
print(f"The word is: {chosen_word}")