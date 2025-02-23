import art
print(art.logo)

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def caeser(original_text,shift,encode_or_decode):
    cipher_text = ""
    for letter in original_text:
        if letter not in alphabet:
            cipher_text += letter
        else:
            if encode_or_decode == "decode":
                shift *= -1
            
            shifted_number = alphabet.index(letter) + shift
            shifted_number %=  len(alphabet)
            cipher_text += alphabet[shifted_number]


    print(f"Here {encode_or_decode}d result text: {cipher_text}")

should_continue = True

while should_continue:   

    direction = input("Type 'encode' to encrypt, 'decode' to decrypt the text \n")
    text = input("Enter the string you want to encrypt/decrypt:").lower()
    shift = int(input("Enter the shift number: "))
    
    # Calling function with keyword arguments
    caeser(original_text=text,shift=shift,encode_or_decode=direction)
    restart = input(("Type 'yes' if you want to continue, else type 'no'\n")).lower()
    if restart == "no":
        should_continue = False
        print("Good Bye!!")
