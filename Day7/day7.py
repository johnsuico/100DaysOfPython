# Creating a hangman game.
import random, stages, word_list

# list of random words.
# word_list = ["ardvark", "baboon", "camel"]

# Choosing a random word.
chosen_word = random.choice(word_list.word_list)

# Generating empty list for guesses.
display = []
for i in chosen_word:
    display += "_"

# Amount of lives
lives = 6

# List for already guessed words
used_letters = []

# Entry logo
print(stages.logo)
print("Welcome to hang man")
print(' '.join(display))

# Check if '_' is still in the list.
while(display.count('_') and lives != 0):
    letter_guess = input("Guess a letter: ").lower()

    # Goes through and checks if letter is in the word.
    # If true, place letter into slot
    for i in range(len(chosen_word)):
        if letter_guess == chosen_word[i]:
            display[i] = letter_guess
    
    # If letter is not in the word, remove a life
    if letter_guess not in chosen_word:
        lives -= 1
        used_letters += letter_guess
        print(f"Lives left: {lives}")

    print(' '.join(display))
    print(stages.stages[lives])
    print(f"Used letters: {' '.join(used_letters)}")

# User won
if '_' not in display and lives != 0:
    print("You've won!")
    print(f"You had {lives} lives left.")

# User lost
if (lives == 0):
    print("You've lost.")

print(f"The word was: {chosen_word.upper()}")