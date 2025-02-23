alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

direction = input("Type 'encode' to encrypt, 'decode' to decrypt the text \n")
shift = int(input("Enter the shift number: "))
text = input("Enter the string you want to encrypt/decrypt:").lower()
# Combining both encode and decode functions

def caeser(original_text,shift,encode_or_decode):
    cipher_text = ""
    for ltr in original_text:
        if encode_or_decode == "decode":
            shift *= -1
        
        shifted_number = alphabet.index(ltr) + shift
        shifted_number %=  len(alphabet)
        cipher_text += alphabet[shifted_number]


    print(f"Here {encode_or_decode}d result text: {cipher_text}")

# Calling function with keyword arguments
caeser(original_text=text,shift=shift,encode_or_decode=direction)

#Calling function with positional arguments
#caeser(text,shift,direction)




'''
#1: Define decrypt() function which takes original_text and shift number
#2: inside decrypt() fucntion , shift the each letter in original_text by shift number given by user 
# and print the decrypt text
#3: call the decrypt function

def encrypt(original_text,shift):
    cipher_text = ""
    for ltr in original_text:
        shifted_number = alphabet.index(ltr) + shift
        shifted_number %=  len(alphabet)
        cipher_text += alphabet[shifted_number]
    
    print(cipher_text)

def decrypt(original_text,shift):
    output_text = ""
    for ltr in original_text:
        shifted_number = alphabet.index(ltr) - shift
        shifted_number %=  len(alphabet)
        output_text += alphabet[shifted_number]
    
    print(output_text)


#decrypt(text,shift)
#encrypt(text,shift)

'''