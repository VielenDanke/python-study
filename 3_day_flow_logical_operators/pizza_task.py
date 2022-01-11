print("Welcome to Python Pizza Deliveries!")
# S = 15 M = 20 L = 25
size = input("What size pizza do you want? S, M, or L ")
# S = 2 M = 3 L = 3
add_pepperoni = input("Do you want pepperoni? Y or N ")
# 1
extra_cheese = input("Do you want extra cheese? Y or N ")

price = 0

if size == "S":
    price += 15
elif size == "M":
    price += 20
else:
    price += 25

if add_pepperoni == "Y":
    if size == "S":
        price += 2
    else:
        price += 3

if extra_cheese == "Y":
    price += 1

print(f"Your final bill is: {price}.")
