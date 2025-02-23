alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

direction = input("Type 'encode' to encrypt, 'decode' to decrypt the text \n")
shift = int(input("Enter the shift number: "))
text = input("Enter the string you want to encrypt/decrypt:").lower()
new_alphabet = []

#1: Create encrypt() function and accepts original_text and shift_number
#2: Inside the encrypt() function forward the each alphabet in original text to the shift number index.
#3: Call the encrypt() function with two arguments
#4: Fix the list index is out of range


#1: Create encrypt() function and accepts original_text and shift_number
def encrypt(original_text,shift):
#2: Inside the encrypt() function forward the each alphabet in original text to the shift number index.
    cipher_text = ""
    for ltr in original_text:
        shifted_number = alphabet.index(ltr) + shift
        #4: Fix the list index is out of range
        shifted_number %=  len(alphabet)
        cipher_text += alphabet[shifted_number]
    
    print(cipher_text)

#3: Call the encrypt() function with two arguments
encrypt(text,shift)



'''
for alp in alphabet:
    shifted = alphabet.index(alp) + shift_number
    if shifted > len(alphabet)-1:
        new_index = shifted - (len(alphabet))
        new_alphabet.append(alphabet[new_index])
    else:
        new_index = shifted
        new_alphabet.append(alphabet[new_index])

new_password = ""
for ltr in password:
    if ltr == " ":
        new_password += ltr
    else:
        new_password += new_alphabet[alphabet.index(ltr)]
'''
