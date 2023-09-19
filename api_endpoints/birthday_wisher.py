import smtplib
import datetime as dt
import random
import csv

#                           CSV FILE

data = [
    {"name": "Amias", "date": "2003-09-19", "email": "amiasyaska@gmail.com"},
    {"name": "Yaska", "date": "2002-09-19", "email": "yasinburhanali@gmail.com"},
    {"name": "Danny", "date": "2001-05-28", "email": "amias@gmail.com"},
    {"name": "John", "date": "2000-01-05", "email": "yaska@gmmail.com"},
]

csv_file_name = "data.csv"
with open(csv_file_name, "w") as file:
    fieldnames = ["name", "date", "email"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    for row in data:
        writer.writerow(row)

all_letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
random_letter = random.choice(all_letters)


with open(random_letter, "r") as template_file:
    template = template_file.read()

#                                       EMAIL TO BE SENT

current_date = dt.datetime.now().day

my_email = "brunodanny2023@gmail.com"
my_password = "bojk qfbz udcs xlhf"

for person in data:
    name = person["name"]
    birth_date = person["date"]
    user_email = person["email"]
    day_part = int(birth_date.split("-")[2])

    if current_date == day_part:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=user_email,
                msg=f"Subject:HAPPY BIRTHDAY\n\n{template.replace('[NAME]', name)}"
            )
