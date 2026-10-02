# Program Name: Assignment2.py
# Course: IT3883/W01
# Student Name: Vince Abraham
# Assignment Number: Assignment 2
# Due Date: 10/02/2026
# Purpose: This program reads student names and six scores from an input file,
# calculates each student's average, and displays the results from highest
# average to lowest average.

# Store each student's name and calculated average.
student_averages = []

# Open the assignment input file and read one student at a time.
with open("Assignment2input.txt", "r") as input_file:
    for line in input_file:
        student_data = line.strip().split()

        # The first value is the student's name. The remaining values are scores.
        student_name = student_data[0]
        student_scores = []

        for score in student_data[1:]:
            student_scores.append(int(score))

        # Calculate the average of the six scores.
        final_average = sum(student_scores) / len(student_scores)
        student_averages.append((student_name, final_average))

# Sort the students by average from highest to lowest.
student_averages.sort(key=lambda student: student[1], reverse=True)

# Display each student's name and average rounded to two decimal places.
for student_name, final_average in student_averages:
    print(f"{student_name} {final_average:.2f}")
