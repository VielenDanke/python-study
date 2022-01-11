import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""

# 2 version

letters_counter = 0
symbols_counter = 0
numbers_counter = 0
num = 0

while True:
    num += 1
    if numbers_counter == nr_numbers and letters_counter == nr_letters and symbols_counter == nr_symbols:
        break
    if num % 2 != 0 and num % 3 != 0 and symbols_counter < nr_symbols:
        password += symbols[random.randint(0, len(symbols) - 1)]
        symbols_counter += 1
    elif num % 2 == 0 and letters_counter < nr_letters:
        password += letters[random.randint(0, len(letters) - 1)]
        letters_counter += 1
    elif num % 3 == 0 and numbers_counter < nr_numbers:
        password += numbers[random.randint(0, len(numbers) - 1)]
        numbers_counter += 1
    else:
        continue

print(password)

# 1 version

password = ""

for num in range(0, nr_letters):
    password = password + letters[random.randint(0, len(letters) - 1)]

for num in range(0, nr_symbols):
    password = password + symbols[random.randint(0, len(symbols) - 1)]

for num in range(0, nr_numbers):
    password = password + numbers[random.randint(0, len(numbers) - 1)]

print(password)
