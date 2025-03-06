

# import datetime as dt
# now = dt.datetime.now()
# new_date = dt.datetime(day=2,month=7,year=2004)
# if new_date.year is now.year:
#     print("You were born this year")
# else:
#     print("You weren't born this year")
# week_day = dt.datetime.weekday(now)
# print(week_day)


import datetime as dt
import smtplib
import random as rd

today = dt.datetime.now()
day = today.weekday()
my_email = "projectemail024@gmail.com"
password = "phhrfytnnzdlsgpx"
with open(file="./quotes.txt") as quotes:
    quote_list = quotes.readlines()
    quote = rd.choice(quote_list)

if day == 4:
    with smtplib.SMTP("smtp.gmail.com") as  connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs=my_email,msg=f"Subject:Monday Motivation\n\n{quote}")
else:
    print(quote)
    print(day)