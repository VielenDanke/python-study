# What was the total bill? $ float
total_bill = round(float(input("What was the total bill? $")), 2)
# What percentage tip would you like to give? 10, 12 or 15? int
percentage_tip = int(input("What percentage tip would you like to give? 10, 12 or 15?"))
# How many people to split the bill? int
amount_people = int(input("How many people to split the bill?"))

total_bill = total_bill * percentage_tip / 100 + total_bill

# Each person should pay: $ float with 2 decimal places
not_rounded_bill = total_bill / amount_people
each_person_bill_format = "{:.2f}".format(not_rounded_bill)
each_person_bill = round(not_rounded_bill, 2)
print(f"Each person should pay: ${each_person_bill_format}")
