import art, os, random

clear = lambda: os.system('cls')

def print_guess(attempts):
    print(f"You have {attempts} attempts remaining to guess the answer.")

def check_guess(guess, answer):
    global ATTEMPTS
    if guess > answer:
        ATTEMPTS -= 1
        print("Too high.")
        print_guess(ATTEMPTS)
        return False
    elif guess < answer:
        ATTEMPTS -=1
        print("Too low.")
        print_guess(ATTEMPTS)
        return False
    elif guess == answer:
        print("You guessed the correct answer.")
        return True

# NUMBER GUESSING GAME

# Easy mode: 10 attempts
# Hard mode: 5 attemps

answer = random.randint(1, 100)

clear()
print(art.logo)

print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 and 100")
mode = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
print(answer)

ATTEMPTS = 0
correct = False

if mode == 'easy':
    ATTEMPTS = 10
    print_guess(ATTEMPTS)
elif mode == 'hard':
    ATTEMPTS = 5
    print_guess(ATTEMPTS)
else:
    ATTEMPTS = 0
    print("You did not enter in a correct difficulty.")

while ATTEMPTS != 0 and correct != True:
    guess = int(input(f"Make a guess: "))
    correct = check_guess(guess, answer)

if ATTEMPTS == 0:
    print("You've run out of guesses, you lose")