# 1 year - 365 days, 52 weeks, 12 months

age = input("What is your current age? ")

age_as_int = int(age)

left_age = 90 - age_as_int

days = left_age * 365
weeks = left_age * 52
months = left_age * 12

calculated_message = f"You have {days} days, {weeks} weeks, and {months} months left"

print(calculated_message)
