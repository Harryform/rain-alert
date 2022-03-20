import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall?"
api_key = "d8eb4159e6671238e5ae02d0f4569edb"
account_sid = "ACbea4ffd4267f5af210bf02f4be2c4f0e"
auth_token = "3203f2eda57a2fb25dc9c2bd3dc39a82"

weather_params = {
    "lat": 32.1491,
    "lon": 81.1632,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data['hourly'][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]['id']
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella!",
        from_='+12694431987',
        to='+15403706668',
    )
    print(message.status)
