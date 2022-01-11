fizz = "Fizz"
buzz = "Buzz"
fizz_buzz = f"{fizz}{buzz}"

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print(fizz_buzz)
    elif num % 3 == 0:
        print(fizz)
    elif num % 5 == 0:
        print(buzz)
    else:
        print(num)
