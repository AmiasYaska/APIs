import datetime as dt
import random
import smtplib

                            # CURRENT DATES
# now = dt.datetime.now()
# current_year = now.year
# current_month = now.month
# day_of_week = now.weekday()             # 0 is monday, 1 is Tuesday
#
# date_of_birth = dt.datetime(year=1977, month=9, day=22)

#                       SENDING WEEKLY QUOTES
with open("quotes.txt") as file:
    line = file.readlines()

    quote_line = random.choice(line)
    print(quote_line)

    now = dt.datetime.now()
    current_day = now.weekday()

    #
    my_email = "abcd@gmail.com"
    my_password = "vmry"

    if current_day == 0:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="xyz@gmail.com",
                msg=f"Subject:PYTHON CODE FOR WEEKLY QUOTES\n\n{quote_line}."
            )
    else:
        print("Quote not sent")

