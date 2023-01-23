import os

PLACEHOLDER = '[name]'

dirname = os.path.dirname(__file__)
name_file = os.path.join(dirname, './Input/Names/invited_names.txt')
letter_file = os.path.join(dirname, './Input/Letters/starting_letter.txt')
output_dir = os.path.join(dirname, './Output/ReadyToSend')

with open(name_file) as data:
    names = data.readlines()

with open(letter_file) as data:
    letter_contents = data.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"{output_dir}/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)