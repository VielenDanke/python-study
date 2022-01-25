import data


def coffee_machine():
    while True:
        user_answer = input("What would you like? (espresso/latte/cappuccino): ")

        if user_answer == "off":
            print("Coffee machine is turning off")
            return

        if user_answer == "report":
            for k in data.resources:
                print(f"{k} {data.resources[k]}")
            continue

        if not is_coffee_exists(user_answer):
            print(f"Coffee {user_answer} is not exists. Try again")
            continue
        else:
            coffee = data.MENU[user_answer]
            if not check_resources(coffee):
                continue
            coins = process_coins()
            if not is_coins_enough(coffee, coins):
                print(f"Sorry that's not enough money {coins}. Money refunded.")
                continue
            make_coffee(coffee, coins)
            process_change(coffee, coins)
            print(f"Here is your {user_answer}. Enjoy!")


def process_change(coffee, coins):
    coins_to_return = round(coins - coffee["cost"], 2)
    if coins_to_return != 0.0:
        print(f"Money to change {coins_to_return}")


def is_coins_enough(coffee, coins):
    return coins > coffee["cost"]


def process_coins():
    coins_amount = {
        "quarters": int(input("How many quarters? ")),
        "dimes": int(input("How many dimes? ")),
        "nickles": int(input("How many nickles? ")),
        "pennies": int(input("How many pennies? ")),
    }
    coins_sum = 0

    for k in data.coins:
        coins_sum += round(coins_amount[k] * data.coins[k], 2)
    return coins_sum


def is_coffee_exists(coffee):
    for k in data.MENU:
        if k == coffee:
            return True
    return False


def check_resources(coffee):
    coffee_resources = coffee["ingredients"]

    for k in coffee_resources:
        if coffee_resources[k] > data.resources[k]:
            print(f"Resource {k} for coffee {coffee_resources['display_name']} not enough")
            return False
    return True


def make_coffee(coffee, coins):
    ingredients = coffee["ingredients"]
    for k in data.resources:
        data.resources[k] = data.resources[k] - ingredients[k]
    data.money += coins


coffee_machine()
