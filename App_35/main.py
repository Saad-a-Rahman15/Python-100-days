import requests
import smtplib
from email.mime.text import MIMEText

OWM_Endpoints = "https://api.openweatherMap.org/data/2.5/forecast"
api_key = "a1f707791cfa41d5131fd911e507383d"

weather_params = {
    "lat": 51.902248,
    "lon": -0.471534,
    "appid": api_key,
    "cnt": 4,
    "units": "metric"
}

response = requests.get(OWM_Endpoints, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
is_hot = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

    current_temp = hour_data["main"]["temp"]
    if current_temp > 23:
        is_hot = True

if will_rain and is_hot:
    text_body = "Weather Alert: It's going to rain today, but it's warm! Bring an umbrella and drink plenty of water! 🌧️🥵"
elif will_rain:
    text_body = "Weather Alert: It is going to rain today! Bring an umbrella. 🌧️"
elif is_hot:
    text_body = "Weather Alert: It's going to be hot today (over 23°C)! Remember to drink water! ☀️🥤"
elif will_rain == False and is_hot == False:
    text_body = "Weather Update: No rain expected today and a comfortable temperature. Enjoy your day! ☀️"

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "saadpy15@gmail.com"
SENDER_PASSWORD = "jatm xfjg rbqm cfcu"

RECEIVER_LIST = [
    "saad.a.rahman15@gmail.com",
    "mmrs151@gmail.com"
]

try:
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(SENDER_EMAIL, SENDER_PASSWORD)

    for receiver in RECEIVER_LIST:
        # Creating a fresh message object inside the loop avoids duplicate headers
        msg = MIMEText(text_body)
        msg["Subject"] = "Daily Weather Notification"
        msg["From"] = SENDER_EMAIL
        msg["To"] = receiver

        server.sendmail(SENDER_EMAIL, receiver, msg.as_string())
        print(f"Success! Notification sent to {receiver}")

    server.quit()

except Exception as e:
    print(f"Could not send. Error details: {e}")