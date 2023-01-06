# Do not use min or max functions
# Only use for loops

def high_score() :
    # Given code
    student_scores = input("\nInput a list of student scores.\n").split(", ")
    for n in range(0, len(student_scores)):
        student_scores[n] = int(student_scores[n])

    # Written code
    max_score = 0
    for score in student_scores :
        if max_score < score :
            max_score = score
    
    print(f"The max score is: {max_score}\n")