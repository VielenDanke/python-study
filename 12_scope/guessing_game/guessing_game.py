from random import randint

from art import logo

START_RANDOM_RANGE = 1
END_RANDOM_RANGE = 100


def print_intro():
    print(logo)
    print("Welcome to guessing game")
    print(f"I think the number is between {START_RANDOM_RANGE} and {END_RANDOM_RANGE}")


def set_difficulty():
    mode = {
        "easy": 10,
        "medium": 7,
        "hard": 5,
    }
    for key in mode:
        print(key)
    return mode[input("Choose the difficulty level ")]


def game():
    print_intro()
    random_number = randint(START_RANDOM_RANGE, END_RANDOM_RANGE)

    print(f"Pssss. Random number is {random_number}")

    difficulty_lvl = set_difficulty()

    print(f"You have {difficulty_lvl} attempts to win the game!")

    for turn in range(0, difficulty_lvl):
        print(f"Turns remaining {difficulty_lvl - turn}")
        if guess(random_number):
            return
    print(f"The number was {random_number}. Try again and WIN!")


def guess(random_number):
    result = False
    guessed_number = int(input("Guess the number? "))
    if guessed_number < random_number:
        print("Too low")
    elif guessed_number > random_number:
        print("Too high")
    else:
        print("You win!")
        result = True
    return result


game()
