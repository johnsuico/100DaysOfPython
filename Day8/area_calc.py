import math

# Written code
def paint_calc(height, width, cover):
    num_cans = math.ceil((height * width) / cover)
    print(f"You'll need {num_cans} cans of paint.")

# Given code
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)