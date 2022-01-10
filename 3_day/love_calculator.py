print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

merged_names = f"{name1}{name2}".lower()

t_counter = 0
l_counter = 0

for c in "true":
    t_counter += merged_names.count(c)

for c in "love":
    l_counter += merged_names.count(c)

score = int(f"{t_counter}{l_counter}")

result_message = ""

if score <= 10 or score >= 90:
    result_message = f"Your score is {score}, you go together like coke and mentos."
elif 40 <= score <= 50:
    result_message = f"Your score is {score}, you are alright together."
else:
    result_message = f"Your score is {score}."

print(result_message)
