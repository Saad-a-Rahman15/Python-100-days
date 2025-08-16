alphabet = list('abcdefghijklmnopqrstuvwxyz')

directions = input("Type 'encode' to encrypt, and type 'decode' to decrypt. \n").lower()
text = input("Type your message: \n").lower()
shift = int(input("Enter the shift number: \n"))

def encrypt(original_text, shift_amount):
    for letter in original_text:
        index_of_letter = alphabet.index(letter)
        encrypted_letter = index_of_letter + shift_amount
    # for encoded_letter in original_text:
        encryption = alphabet[encrypted_letter]
        print(encryption, end='')
                        
encrypt(text, shift)

print('')
