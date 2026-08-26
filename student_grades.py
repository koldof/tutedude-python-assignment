students = {
    "Alice": 85,
    "Bob": 90
}

# Add a new student
name = input("Enter new student name: ")
grade = int(input("Enter grade: "))

if name in students:
    print("Student already exists.")
else:
    students[name] = grade
    print("Student added successfully.")

# Update a student's grade
name = input("Enter student name to update: ")

if name in students:
    new_grade = int(input("Enter new grade: "))
    students[name] = new_grade
    print("Grade updated successfully.")
else:
    print("Student not found.")

# Print all student grades
print("\nAll Student Grades:")

for name, grade in students.items():
    print(name, ":", grade)