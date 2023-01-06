import random

def rock_paper_scissors() :
    rock = '''
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
            ______)
            _______)
            _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    '''

    game_images = [rock, paper, scissors]

    print("Welcome to rock, paper, scissors.")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    user_choice = int(input("Please enter the corresponding number."))-1

    computer_choice = random.randint(0, 2)

    print("You chose: ")
    print(game_images[user_choice])

    print("Computer chose:")
    print(game_images[computer_choice])

    if (user_choice >= 4 or user_choice <= 0) :
        print("You didn't enter in a valid choice.")
    elif (user_choice == 1 and computer_choice == 2) :
        print("You lost.")
    elif (user_choice == 1 and computer_choice == 3) :
        print("You won.")
    elif (user_choice > computer_choice) :
        print("You won.")
    elif (user_choice < computer_choice) :
        print("You lost.")
    elif (user_choice == computer_choice) :
        print("It's a draw.")