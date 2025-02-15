import random

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
           "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers = ["1","2","3","4","5","6","7","8","0"]
symbols = ["!","@","#","$","%","&","*","(",")","+","_"]

print("Welcome to PyPassword Generator!")
nr_letters = int(input("How letters would you like in password? "))
nr_symbols = int(input("How symbols would you like in password? "))
nr_numbers = int(input("How numbers would you like in password? "))

# Easy Level : All letters, numbers and symbols are in sequence.
# e.g: a#0fI#RO8K
# afIRKO##08

passwd = ""
for letter in range(nr_letters):
    passwd += random.choice(letters)

for sym in range(nr_symbols):
    passwd += random.choice(symbols)

for num in range(nr_numbers):
    passwd += random.choice(numbers)

print(f"Your easy password is: {passwd}")

# Hard Level: all letters,numbers, symbols are scattered or randomised.
# e.g,: a#0fI#RO8K

passwd_lst = []
for letter in range(nr_letters):
    passwd_lst += random.choice(letters)

for sym in range(nr_symbols):
    passwd_lst += random.choice(symbols)

for num in range(nr_numbers):
    passwd_lst += random.choice(numbers)

random.shuffle(passwd_lst)

password = ""
for item in passwd_lst:
    password += item

print(f"Your Hard password is: {password}")
