# Python_assignment5
*********************************Task 1***************************
-> Write a dictionary program with student name and their mark
# Create a dictionary with student names with his marks
student_marks = {
    "Ravi": 85,
    "Sneha": 92,
    "Amit": 76,
    "Priya": 89,
    "Karan": 95,
    "Rakesh": 69
}
-> Ask the user to input a student's name
name = input("Enter the student's name: ")

-> Retrieve and display marks or show an appropriate message
if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print("Student not found in the records.")
******************output******************
C:\Users\RAKESH\AppData\Local\Microsoft\WindowsApps\python3.13.exe D:\tutedude_python\Assignment_5\main.py 
Enter the student's name: Rakesh
Rakesh's marks: 69

******************************task 2******************************

-> write a program take input from user 1 to 10 and extract first 5 number and reverser 
that extracting no.
->Create a list of numbers from 1 to 10
numbers = list(range(1, 10))

->#Extract the first five elements
extracted_list = numbers[:5]

->Reverse the extracted elements
reversed_list = extracted_list[::-1]

->Printing extracted_list and reversed_list
print("Extracted first 5 List:", extracted_list)
print("Reversed extracted List:", reversed_list)

********************output********************
C:\Users\RAKESH\AppData\Local\Microsoft\WindowsApps\python3.13.exe D:\tutedude_python\Assignment_5\slice.py 
Extracted first 5 List: [1, 2, 3, 4, 5]
Reversed extracted List: [5, 4, 3, 2, 1]
