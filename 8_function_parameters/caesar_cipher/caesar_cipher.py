from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def is_direction_valid(direction):
    return direction == "encode" or direction == "decode"


def is_shift_valid(shift):
    return shift > len(alphabet)


def is_word_valid(word):
    for char in word:
        if char not in alphabet:
            return False
    return True


def caesar(text, shift, direction):
    result = ""
    if direction == "decode":
        shift *= -1
    for char in text:
        idx = alphabet.index(char)
        result_idx = idx + shift
        if result_idx >= len(alphabet):
            result_idx = result_idx - len(alphabet)
        result += alphabet[result_idx]
    return result


print(logo)

is_end = False

direction = ""

while not is_end:
    if len(direction) == 0:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

        if not is_direction_valid(direction):
            print(f"Operation unknown: {direction}")
            direction = ""
            continue
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if not is_word_valid(text):
        print(f"Word is not valid: {text}. Use only letters")
    elif not is_shift_valid(shift):
        print(f"Shift is not valid: {shift}. Try to input number lower than 27")
    else:
        print(f"Result of operation {direction} is word: {caesar(text=text, shift=shift, direction=direction)}")
        is_continue = input("Do you want to continue? Type 'yes' or 'no'").lower()
        if is_continue == "no":
            is_end = True
        direction = ""
