import random


def game():
    word_list = ["aardvark", "baboon", "camel"]

    guess_word = random.choice(word_list)

    empty_guess_list = []

    for i in range(0, len(guess_word)):
        empty_guess_list.append("_")

    while True:
        guess_letter = input("Guess the letter? ")

        if not validate_letter_length(guess_letter):
            print("Insert only one letter")
            continue

        correct_idx = check_letter(guess_letter, guess_word)

        if len(correct_idx) == 0:
            print("Wrong")
        else:
            for i in correct_idx:
                empty_guess_list[i] = guess_word[i]
            print(empty_guess_list)


def validate_letter_length(letter):
    return len(letter) == 1


def check_letter(letter, word):
    correct_idx = []
    for idx in range(0, len(word)):
        if word[idx] == letter:
            correct_idx.append(idx)
    return correct_idx


game()
