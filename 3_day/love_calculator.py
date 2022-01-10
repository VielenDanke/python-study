print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

mergeNames = f"{name1}{name2}".lower()

tCounter = 0
lCounter = 0

for c in "true":
    tCounter += mergeNames.count(c)

for c in "love":
    lCounter += mergeNames.count(c)

score = int(f"{tCounter}{lCounter}")

resultMessage = ""

if score <= 10 or score >= 90:
    resultMessage = f"Your score is {score}, you go together like coke and mentos."
elif 40 <= score <= 50:
    resultMessage = f"Your score is {score}, you are alright together."
else:
    resultMessage = f"Your score is {score}."

print(resultMessage)
