import requests
import os
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        if response.status_code == 200:
            print(f"\nWeather in {data['name']}, {data['sys']['country']}:")
            print(f" Temperature: {data['main']['temp']}°C")
            print(f" Weather: {data['weather'][0]['description'].capitalize()}")
            print(f" Wind Speed: {data['wind']['speed']} m/s\n")
        else:
            print(f" Error: {data.get('message', 'Something went wrong.')}")
    except requests.exceptions.RequestException as e:
        print(f" Request failed: {e}")

if __name__ == "__main__":
    while True:
        city = input("Enter city name (or 'exit' to quit): ").strip()
        if city.lower() == 'exit':
            break
        elif city:
            get_weather(city)
        else:
            print("Please enter a valid city name.")
