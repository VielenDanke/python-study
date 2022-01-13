from art import logo

print(logo)
print("Welcome to blind auction")

bids = {}

temp_name = ""

while True:
    if len(temp_name) == 0:
        temp_name = input("What is your name? ")

    if len(temp_name) == "":
        print("Please input name")
        continue

    bid = int(input(f"What is your bid? {temp_name} $"))

    if bid < 1:
        print("Bid cannot be less than 1")
        continue
    bids[temp_name] = bid

    is_one_more = input("One more participant? Type 'yes' or 'no' ")

    if is_one_more == 'no':
        break
    temp_name = ""

if len(bids) > 0:
    max_bid_person_name = ""
    max_bid = 0

    for person_name in bids:
        person_bid = bids[person_name]
        if person_bid > max_bid:
            max_bid_person_name = person_name
            max_bid = person_bid

    print(f"Person {max_bid_person_name} win with bid {max_bid}")
else:
    print("Empty list. No participants detected")
