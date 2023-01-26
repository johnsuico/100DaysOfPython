import smtplib

# Email and password fields are left empty for security.

with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
    connection.starttls()
    connection.login(user='', password='')
    connection.sendmail(
        from_addr='', 
        to_addrs='', 
        msg='Subject:Hello \n\nThis is the body of my email.'
    )