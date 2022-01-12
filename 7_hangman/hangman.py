import random
from hangman_art import stages, logo
from hangman_words import word_list


def game():
    life_counter = len(stages) - 1

    guess_word = random.choice(word_list)

    empty_guess_list = []
    guessed_letters = []

    for _ in range(0, len(guess_word)):
        empty_guess_list.append("_")

    lose_condition = 0

    print(logo + "\n")

    print(f"Pssss. The solution is {guess_word}")

    while life_counter > lose_condition:
        if "_" not in empty_guess_list:
            break

        letter = input("Guess the letter? ").lower()

        if not validate_letter_length(letter):
            print("Insert only one letter")
            continue
        if letter in guessed_letters:
            print("You already guessed this letter. Choose another one")
            continue

        guessed_letters.append(letter)

        is_found = set_letter_if_exists(letter, guess_word, empty_guess_list)

        if is_found:
            print("You guessed right!")
            # join list into a string with space between each array element
            print(f"{' '.join(empty_guess_list)}")
            print(stages[life_counter])
            continue
        life_counter -= 1
        print(f"You guessed a letter {letter} that is not in the word. You lose a life.")
        print(f"{' '.join(empty_guess_list)}")
        print(stages[life_counter])
    if life_counter > lose_condition:
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
