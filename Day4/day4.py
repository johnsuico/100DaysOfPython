import coin_toss
import treasure_map
import rock_paper_scissors

def menu_map(choice) :
    if (choice == 1) :
        coin_toss.coin_toss()
    elif (choice == 2) :
        treasure_map.treasure_map()
    elif (choice == 3) :
        rock_paper_scissors.rock_paper_scissors()

print("\n\nWelcome to the 4th day of 100 Days of Python.")
print("Enter in the number for a certain exercise for this day.")

while (True) :
    print("1. Coin toss")
    print("2. Treasure map")
    print("3. Rock, paper, scissors")
    print("4. Exit program")

    choice = int(input())
    if (choice <= 0 or choice >= 4) :
        print("Goodbye!")
        break
    else :
        menu_map(choice)