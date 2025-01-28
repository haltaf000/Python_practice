alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift_amount, direction):
    if direction == "encode":
        new_text = ''
        for letter in text:
            if letter in alphabet:
                current_position = alphabet.index(letter)
                shift = (current_position + shift_amount) % 26
                new_letters = alphabet[shift]
                new_text += new_letters
        print(f"Here is the encoded result: {new_text}")

    if direction == "decode":
        de_cipher_text = ""
        for letter in text:
            if letter in alphabet:
                current_position = alphabet.index(letter)
                shift = (current_position - shift_amount) % 26
                new_letters = alphabet[shift]
                de_cipher_text  += new_letters
        print(f"Here is the decoded result: {de_cipher_text}")

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.").lower()

    if restart == "no":
        should_continue = False
        print("Goodbye!")