import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


def game():
    life_counter = len(stages) - 1

    word_list = ["aardvark", "baboon", "camel"]

    guess_word = random.choice(word_list)

    empty_guess_list = []

    for _ in range(0, len(guess_word)):
        empty_guess_list.append("_")

    lose_condition = 0

    while life_counter > lose_condition:
        if "_" not in empty_guess_list:
            break

        guess_letter = input("Guess the letter? ")

        if not validate_letter_length(guess_letter):
            print("Insert only one letter")
            continue
        if guess_letter in empty_guess_list:
            print("You already guessed this letter. Choose another one")
            continue

        is_found = set_letter_if_exists(guess_letter, guess_word, empty_guess_list)

        if is_found:
            print(empty_guess_list)
            continue
        life_counter -= 1
        print(stages[life_counter])
    if life_counter < lose_condition:
        print("You win!")
        return
    print("You lose!")


def validate_letter_length(letter):
    return len(letter) == 1


def set_letter_if_exists(letter, word, empty_guess_list):
    is_found = False
    for idx in range(0, len(word)):
        if word[idx] == letter:
            empty_guess_list[idx] = word[idx]
            is_found = True
    return is_found


game()
