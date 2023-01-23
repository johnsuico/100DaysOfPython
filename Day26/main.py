import pandas as pd
import os

dirname = os.path.dirname(__file__)
nato_path = os.path.join(dirname, './nato_phonetic_alphabet.csv')

nato_data = pd.read_csv(nato_path)

nato_dict = {row.letter:row.code for (index, row) in nato_data.iterrows()}

user_word = input("Enter a word: ").upper()

result = [nato_dict[letter] for letter in user_word]

print(result)