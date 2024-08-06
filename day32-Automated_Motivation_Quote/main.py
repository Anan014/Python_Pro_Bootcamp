import smtplib
import datetime as dt
import random

my_email = "anan18am@gmail.com"
password = ""

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = [quote for quote in quote_file.readlines()]
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="anan18am@yahoo.com",
            msg=f"Subject:Monday Motivation\n\n{quote}")




