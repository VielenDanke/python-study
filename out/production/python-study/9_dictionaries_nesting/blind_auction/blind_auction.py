from art import logo

print(logo)
print("Welcome to blind auction")

persons = []

temp_name = ""
temp_bid = 0

while True:
    if len(temp_name) == 0:
        temp_name = input("What is your name? ")

    if len(temp_name) == "":
        print("Please input name")
        continue

    temp_bid = int(input("What is your bid? $"))

    if temp_bid < 1:
        print("Bid cannot be less than 1")
        continue

    person = {
        "name": temp_name,
        "bid": temp_bid,
    }
    persons.append(person)

    is_one_more = input("One more participant? Type 'yes' or 'no' ")

    if is_one_more == 'no':
        break
    temp_name = ""
    temp_bid = 0

if len(persons) > 0:
    max_bid_person_name = persons[0]["name"]
    max_bid = persons[0]["bid"]

    for idx in range(1, len(persons)):
        person = persons[idx]
        person_bid = person["bid"]
        if person_bid > max_bid:
            max_bid_person_name = person["name"]
            max_bid = person_bid

    print(f"Person {max_bid_person_name} win with bid {max_bid}")
print("Empty list. No participants detected")
