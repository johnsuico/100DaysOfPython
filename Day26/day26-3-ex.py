import os

dirname = os.path.dirname(__file__)
file_one_path = os.path.join(dirname, './file1.txt')
file_two_path = os.path.join(dirname, './file2.txt')

with open(file_one_path) as file_one:
    file_one_data = file_one.readlines()

with open(file_two_path) as file_two:
    file_two_data = file_two.readlines()

# Goal: Use list comprehension to create a new list of values that are presnet in both files

# Turn the lists content into ints
file_one_data = [int(num) for num in file_one_data]
file_two_data = [int(num) for num in file_two_data]

results = [num for num in file_one_data if num in file_two_data]

print(results)