import smtplib

my_username = "abc@gmail.com"
my_password = "123"

with smtplib.SMTP("smtp.gmail.com", 587) as connection:         # 587 is the smtp_port
    connection.starttls()
    connection.login(user=my_username, password=my_password)
    connection.sendmail(
        from_addr=my_username,                                  # email of the sender
        to_addrs="dfgh@gmail.com",                              # email of the receiver
        msg="Subject:From python code\n\nThis was sent the day I passed my AWS"
            "Certified Cloud Practitioner exam."
    )
