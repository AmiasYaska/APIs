import requests
from datetime import datetime
import smtplib

MY_LAT = 0.347596
MY_LONG = 32.582520

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour



if (MY_LAT - 5) <= iss_latitude <= (MY_LAT + 5) and (MY_LONG - 5) < iss_longitude < (MY_LONG + 5):
    if time_now >= sunset or time_now <= sunrise:
        with smtplib.SMTP("gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user="brunodanny2023@gmail.com", password="2023")
            connection.sendmail(
                from_addr="br@gmail.com",
                to_addrs="br@gmail.com",
                msg="Subject: ISS IS CLOSE\n\nLook up and see the ISS."
            )
