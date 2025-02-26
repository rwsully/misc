#This is for the nerds out there, recently have been watching a few spy movies and found it very intresting how they would encrypt messages.
#Decided to give it a crack myself, I have tried to explain the code as best as i could, i don't work with python usally so this was a learning experience for me.

import random

def custom_encoder(input_text):
    result = []
    shift_letter = 3  # Starting shift for letters
    shift_digit = 2  # Starting shift for digits
    shift_symbol = 1  # Starting shift for symbols
    random.seed(42)  # For reproducibility
    
    for idx, char in enumerate(input_text):
        if char.isalpha():  # Check if the character is a letter
            if char.islower():
                # Reverse the alphabet and shift by a non-linear amount
                encoded_char = chr(219 - ord(char) + shift_letter)
                shift_letter = (shift_letter + 2) % 26  # Change shift dynamically for next letter
            elif char.isupper():
                # Reverse the alphabet and shift by a non-linear amount
                encoded_char = chr(155 - ord(char) + shift_letter)
                shift_letter = (shift_letter + 2) % 26  # Change shift dynamically for next letter
            # Apply XOR transformation to further obscure the result
            encoded_char = chr(ord(encoded_char) ^ random.randint(10, 50))  # XOR with random value
            result.append(encoded_char)
        elif char.isdigit():  # For digits, apply a reverse and shift
            # Reverse digits and apply a shift dynamically
            encoded_char = str((9 - int(char) + shift_digit) % 10)
            shift_digit = (shift_digit + 2) % 10  # Change shift dynamically for next digit
            result.append(encoded_char)
        else:
            # Apply a transformation to symbols by modifying ASCII dynamically
            encoded_char = chr(ord(char) + shift_symbol)
            shift_symbol = (shift_symbol + 1) % 10  # Increment the shift for symbols
            result.append(encoded_char)
    
    return ''.join(result)

def custom_decoder(encoded_text):
    result = []
    shift_letter = 3  # Starting shift for letters
    shift_digit = 2  # Starting shift for digits
    shift_symbol = 1  # Starting shift for symbols
    random.seed(42)  # For reproducibility
    
    for idx, char in enumerate(encoded_text):
        if char.isalpha():  # Check if the character is a letter
            # Reverse XOR transformation to decode
            decoded_char = chr(ord(char) ^ random.randint(10, 50))  # XOR with same random value
            
            if decoded_char.islower():
                # Reverse the alphabet and shift back by a non-linear amount
                decoded_char = chr(219 - ord(decoded_char) - shift_letter)
                shift_letter = (shift_letter + 2) % 26  # Change shift dynamically for next letter
            elif decoded_char.isupper():
                # Reverse the alphabet and shift back by a non-linear amount
                decoded_char = chr(155 - ord(decoded_char) - shift_letter)
                shift_letter = (shift_letter + 2) % 26  # Change shift dynamically for next letter
            result.append(decoded_char)
        elif char.isdigit():  # For digits, reverse the transformation
            decoded_char = str((9 - int(char) - shift_digit) % 10)
            shift_digit = (shift_digit + 2) % 10  # Change shift dynamically for next digit
            result.append(decoded_char)
        else:
            # Reverse the transformation for symbols
            decoded_char = chr(ord(char) - shift_symbol)
            shift_symbol = (shift_symbol + 1) % 10  # Decrement the shift for symbols
            result.append(decoded_char)
    
    return ''.join(result)

def main():
    while True:
        choice = input("Do you want to (e)ncode or (d)ecode a message? (q to quit): ").lower()
        if choice == 'q':
            break
        elif choice == 'e':
            user_input = input("Enter the text to encode: ")
            encoded_text = custom_encoder(user_input)
            print("Encoded text:", encoded_text)
        elif choice == 'd':
            user_input = input("Enter the text to decode: ")
            decoded_text = custom_decoder(user_input)
            print("Decoded text:", decoded_text)
        else:
            print("Invalid choice. Please enter 'e' to encode, 'd' to decode, or 'q' to quit.")

if __name__ == "__main__":
    main()

