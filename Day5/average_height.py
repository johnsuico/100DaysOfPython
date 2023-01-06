# Restrictions: No sum function or len function
# Only use for loops

def average_height() :
    # Given code
    student_heights = input("\nInput a list of student heights: \n").split(", ")
    for n in range(0, len(student_heights)) :
        student_heights[n] = int(student_heights[n])

    # Written code
    height_sum = 0
    listLength = 0
    for height in student_heights :
        height_sum += height
        listLength += 1

    average = height_sum / listLength

    print(f"The average student height is: {average}\n")