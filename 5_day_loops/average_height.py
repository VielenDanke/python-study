student_heights = input("Input a list of student heights ").split()
for i in range(0, len(student_heights)):
    student_heights[i] = int(student_heights[i])

num_of_students = 0
total_height = 0

for height in student_heights:
    total_height += height
    num_of_students += 1

print(round(total_height / num_of_students))

# alternative solution

print(round(sum(student_heights) / len(student_heights)))
