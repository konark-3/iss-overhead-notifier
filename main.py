import time
import requests
import datetime as dt
import smtplib

LAT = 53.544388
LONG = -113.490929
EMAIL = "konnarkmalhottra@gmail.com"
PASSWORD = "gjdtwsnhxvanyckn"


def is_iss_overhead():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    long = float(data['iss_position']['longitude'])
    lat = float(data['iss_position']['latitude'])

    if abs(lat-LAT) <= 5 and abs(long-LONG) <= 5:
        return True


def is_night():
    parameters = {
        'lat': LAT,
        'lng': LONG,
        'formatted': 0
    }

    endpoint = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    endpoint.raise_for_status()
    info = endpoint.json()
    sunrise = int(info['results']['sunrise'].split("T")[1].split(":")[0])
    sunset = int(info['results']['sunset'].split("T")[1].split(":")[0])

    time_now = dt.datetime.now().hour

    if sunset < time_now < sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=EMAIL, to_addrs="konnarkmalhottra@yahoo.com", msg="Subject:Look up\n\n Notification")





