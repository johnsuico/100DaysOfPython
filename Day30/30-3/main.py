# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas, os

nato_data_path = os.path.join(os.path.dirname(__file__), './nato_phonetic_alphabet.csv')

data = pandas.read_csv(nato_data_path)

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

def gen_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print('Sorry, only letter in the alphabet please.')
        gen_phonetic()
    else:
        print(output_list)

gen_phonetic()