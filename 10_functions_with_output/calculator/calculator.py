from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 == 0:
        return "Cannot divide to 0"
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

print(logo)


def calculator():
    is_continue = True

    num1 = float(input("Insert the number?: "))

    for k in operations:
        print(k)

    while is_continue:
        user_operation_symbol = input("Pick an operation?: ")
        num2 = float(input("What is the next number?: "))

        result = operations[user_operation_symbol](num1, num2)
        print(f"{num1} {user_operation_symbol} {num2} = {result}")
        num1 = result
        user_answer = input("Do you want to continue? Type 'y' or 'n' to start a new operation. To stop the program - "
                            "type any symbol instead ")
        if user_answer == "n":
            is_continue = False
            calculator()
        elif user_answer != "y":
            print("Unknown answer. Exit program")
            return num1


print(f"Final result: {calculator()}")
