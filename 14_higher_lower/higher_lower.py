from random import randint
import art
from game_data import data


def choice_persons():
    random_persons = []
    f_idx = randint(0, len(data) - 1)
    s_idx = randint(0, len(data) - 1)
    while f_idx == s_idx:
        f_idx = randint(0, len(data) - 1)
        s_idx = randint(0, len(data) - 1)
    random_persons.append(data[f_idx])
    random_persons.append(data[s_idx])
    return random_persons


def compare_persons(person_a, person_b, user_answer):
    if person_a["follower_count"] > person_b["follower_count"]:
        return user_answer == "A"
    elif person_a["follower_count"] < person_b["follower_count"]:
        return user_answer == "B"
    else:
        return True


def game():
    print(art.logo)

    is_person_right = True
    score = -1

    while is_person_right:
        score += 1
        persons = choice_persons()
        person_a = persons[0]
        person_b = persons[1]
        print(f"Compare A: {person_a['name']}, {person_a['description']}, {person_a['country']}")
        print(art.vs)
        print(f"Compare B: {person_b['name']}, {person_b['description']}, {person_b['country']}")
        user_answer = input("Who has more followers? Type 'A' or 'B' ").upper()
        is_person_right = compare_persons(person_a, person_b, user_answer)
    print(f"Sorry, that is wrong. Final score: {score}")


game()
