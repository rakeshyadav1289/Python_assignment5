# Create a dictionary with student names with his marks
student_marks = {
    "Ravi": 85,
    "Sneha": 92,
    "Amit": 76,
    "Priya": 89,
    "Karan": 95,
    "Rakesh": 69
}

#Ask the user to input a student's name
name = input("Enter the student's name: ")

#Retrieve and display marks or show an appropriate message
if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print("Student not found in the records.")
