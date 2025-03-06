##################### Extra Hard Starting Project ######################
import smtplib

import pandas as pd
import datetime as dt
from random import randint as rd
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
data = pd.read_csv("birthdays.csv")
data_dict = data.to_dict(orient="records")
num = rd(1,3)

day = dt.datetime.now()
to_month = day.month
to_day = day.day

for i in range(len(data_dict)):
    person_detail = data_dict[i]
    if person_detail["month"] == to_month and person_detail["day"] == to_day:
        person_name = person_detail["name"]
        with open(file=f"letter_templates/letter_{num}.txt") as letter:
            sentences = letter.read()
            new_letter = sentences.replace("[NAME]", f"{person_name}")

            print(new_letter)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=person_detail["email"], password="xzeddanljneahkoi")
            connection.send_message(from_addr="kobbygilbert233@gmail.com",to_addrs=person_detail["email"],msg=new_letter)



# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv




# 4. Send the letter generated in step 3 to that person's email address.




