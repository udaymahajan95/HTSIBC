#count no of student that passed.
print("Count the numberds of student which are got greater then 50 marks.")
marks_of_student = [55, 42, 77, 63, 29, 57, 89]
count = 0
i = 0

while count < len(marks_of_student):
    if marks_of_student[i] > 50:
        count += 1
        i += 1
print(f"Numbers of students who passed: {count}")