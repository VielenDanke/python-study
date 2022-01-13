alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
    result = ""
    for char in plain_text:
        idx = alphabet.index(char)
        cipher_idx = idx + shift_amount
        if cipher_idx >= len(alphabet):
            cipher_idx = cipher_idx - len(alphabet)
        result += alphabet[cipher_idx]
    return result


def decrypt(cipher_text, shift_amount):
    result = ""
    for char in cipher_text:
        cipher_idx = alphabet.index(char)
        idx = cipher_idx - shift_amount
        result += alphabet[idx]
    return result


if direction == "encode":
    print(f"The encoded text is {encrypt(plain_text=text, shift_amount=shift)}")
elif direction == "decode":
    print(f"The decoded text is {decrypt(cipher_text=text, shift_amount=shift)}")
else:
    print("Unknown direction")

