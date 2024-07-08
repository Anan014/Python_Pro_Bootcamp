from art import logo

print(logo)


def caesar(text, shift, direction):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    output_word = ""

    # Normalize the shift to stay within the range of 0-25
    shift = shift % len(alphabet)
    if direction.lower() == "decode":
        shift = -shift

    for letter in text:
        if letter in alphabet:
            letter_place = alphabet.index(letter)
            new_place = (letter_place + shift) % len(alphabet)
            output_word += alphabet[new_place]
        else:
            output_word += letter  # Keep non-alphabet characters unchanged

    print(output_word)


isAgain = True
while isAgain:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    result = input("Type 'yes' if you want to go again. Otherwise type 'no': ").lower()
    if result == "no":
        isAgain = False
        print("Good bye!")
