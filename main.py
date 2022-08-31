import requests
import os
from twilio.rest import Client

OWM_API_KEY = os.environ.get('OWM_API')
MY_LAT = 48.856613
MY_LONG = 2.352222

TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_AUTH = os.environ.get("TWILIO_AUT")

PHONE = os.environ.get("PHONE")

response = requests.get(f"https://api.openweathermap.org/data/3.0/onecall?lat={MY_LAT}&lon={MY_LONG}&appid={OWM_API_KEY}"
                        f"&exclude=current,minutely,daily")
response.raise_for_status()
data = response.json()

UMBRELLA_NEEDED = ["Rain", "Drizzle", "Thunderstorm"]


def rain_today():
    rain = False
    for forecast in data["hourly"][:12]:
        weather = forecast["weather"][0]["main"]
        if weather in UMBRELLA_NEEDED:
            rain = True
            return rain
    return rain


accound_sid = TWILIO_SID
auth_token = TWILIO_AUTH
client = Client(accound_sid, auth_token)

if rain_today():
    client = Client(accound_sid, auth_token)
    message = client.messages \
        .create(
            body="It might rain today, bring an umbrella",
            from_="+12184025227",
            to=PHONE,
    )


