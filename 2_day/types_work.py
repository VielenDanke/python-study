num_char = len(input("What is your name?"))
test_str = "Test string"

# show the type of variable
print(type(num_char))

# type casting
num_char_str = str(num_char)
fl = float(num_char)
reverse_casting_int = int(num_char_str)

print("Your name has " + num_char_str + " characters.")
print(fl)
print(reverse_casting_int)
