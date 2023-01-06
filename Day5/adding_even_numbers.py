def adding_even_numbers() :
    even_sum = 0
    for even in range(0, 101, 2) :
        even_sum += even
    print(f"The sum of the even numbers from 1 - 100 = {even_sum}")