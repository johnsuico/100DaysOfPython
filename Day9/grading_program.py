# Goal: To familiarize with python dictionaries
# Based on student scores create a new dictionary with a comment about their score

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for key in student_scores:
    if student_scores[key] >= 91 and student_scores[key] <= 100:
        student_grades[key] = "Outstanding"
    elif student_scores[key] >= 81 and student_scores[key] <= 90:
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] >= 71 and student_scores[key] <= 80:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

print(student_grades)