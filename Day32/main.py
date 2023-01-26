import datetime as dt, random, pandas as pd, os, smtplib

# Get all the file paths
dirname = os.path.dirname(__file__)
birthday_data_path = os.path.join(dirname, './birthdays.csv')

# Getting todays date
date = dt.datetime.now()
today = (date.month, date.day)

# Open birthdays.csv
birthday_data = pd.read_csv(birthday_data_path)
birthday_dict = {(data_row['month'], data_row['day']):data_row for (index, data_row) in birthday_data.iterrows()}

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    random_letter_path = os.path.join(dirname, f'./letter_templates/letter_{random.randint(1, 3)}.txt')
    with open(random_letter_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person['name'])
        print(contents)

    # Fields left empty for security
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user='', password='')
        connection.sendmail(
            from_addr='',
            to_addrs=birthday_person['email'],
            msg=f'Subject:Happy Birthday\n\n{contents}'
        )