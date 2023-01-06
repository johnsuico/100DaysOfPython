import average_height, high_score, adding_even_numbers, fizzbuzz, password_gen

def menu_map(choice) :
    if (choice == 1) :
        average_height.average_height()
    elif (choice == 2) :
        high_score.high_score()
    elif (choice == 3) :
        adding_even_numbers.adding_even_numbers()
    elif (choice == 4) :
        fizzbuzz.fizzbuzz()
    elif (choice == 5) :
        password_gen.password_gen()

print("\n\nWelcome to the 5th day of 100 Days of Python.")
print("Enter in the number for a certain exercise for this day.")

while (True) :
    print("1. Average Height")
    print("2. High Score")
    print("3. Adding Even Numbers")
    print("4. FizzBuzz Job Interview Question")
    print("5. Password Generator")
    print("6. Exit Program")

    choice = int(input())
    if (choice <= 0 or choice >= 6) :
        print("Goodbye!")
        break
    else :
        menu_map(choice)