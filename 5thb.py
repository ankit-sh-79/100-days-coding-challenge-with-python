#input a python list of student heights
student_heihgts = input().aplit()
for n in range(0, len(student_heihgts)):
    student_heihgts[n] = int(student_heihgts[n])
#your code below this row
total_height = 0
for height in student_heihgts:
    total_height += height
print(f"Total height = {total_height}")

number_of_students = 0
for student in student_heihgts:
    number_of_students += 1
print(f"Number of students = {number_of_students}")

average_height = round(total_height / number_of_students)
print(f"Average height = {average_height}")





#your code above this row