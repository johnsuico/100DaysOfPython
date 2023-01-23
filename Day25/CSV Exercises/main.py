import os
import pandas as pd

dirname = os.path.dirname(__file__)
squirrel_path = os.path.join(dirname, './squirrel.csv')

squirrel_data = pd.read_csv(squirrel_path)

gray_squirrel_count = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Gray'])
black_squirrel_count = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Black'])
cinnamon_squirrel_count = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Cinnamon'])

squirrel_dict = {
    'Fur Color' : ['Gray', 'Cinnamon', 'Black'],
    'Count': [gray_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]
}

df = pd.DataFrame(squirrel_dict)
df.to_csv('squirrel_count.csv')