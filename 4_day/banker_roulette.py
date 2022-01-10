import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

random_roulette_number = random.randint(0, len(names) - 1)

print(f"{names[random_roulette_number]} is going to buy the meal today!")
