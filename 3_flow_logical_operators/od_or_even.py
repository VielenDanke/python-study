num = int(input("Which number do you want to check? "))

if num % 2 == 0:
    print("This is an even number")
elif num % 2 != 0:
    print("This is an odd number")
else:
    print("Something went wrong")
