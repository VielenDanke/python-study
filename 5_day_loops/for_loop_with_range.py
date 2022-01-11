# range (x included, y excluded, z - step of increment)

for num in range(1, 11):
    print(num)

for num in range(1, 11, 3):
    print(num)

total = 0

for num in range(1, 101):
    total += num

print(total)
