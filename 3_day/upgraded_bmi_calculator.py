height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / height ** 2)

if bmi < 18.5:
    print(f"underweight. bmi {bmi}")
elif bmi < 25:
    print(f"normal weight. bmi {bmi}")
elif bmi < 30:
    print(f"overweight. bmi {bmi}")
elif bmi < 35:
    print(f"obese. bmi {bmi}")
else:
    print(f"clinically obese. bmi {bmi}")
