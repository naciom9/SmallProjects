from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:  # Account for number/symbol/space
            end_text += char

    print(f"Here's the {cipher_direction}d result: {end_text}")


# Import and print the logo from art.py
print(logo)

# While loop that continues to execute the program if the user types 'yes'.
start_selection = True
while start_selection:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
# Code to help when a user enters a shift that is greater than the number of letters in the alphabet?
    shift = shift % 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    result = input("Do you want to play again? Type 'yes' or 'no': ").lower()
    if result == "no":
        start_selection = False
        print("Thanks for using Naciom9 Cipher. Goodbye!")
