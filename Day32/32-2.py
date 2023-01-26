import datetime as dt
import os, random, smtplib

dirname = os.path.dirname(__file__)
quote_path = os.path.join(dirname, './quotes.txt')

date = dt.datetime.now()

with open(quote_path, 'r') as data:
    quotes = data.readlines()

# Checks if the weekday is Monday
if date.weekday() == 0:
    random_quote = random.choice(quotes)

    # Fields are left empty for security.
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user='', password='')
        connection.sendmail(
            from_addr='',
            to_addrs='',
            msg=f'Subject:Quote\n\n{random_quote}'
        )