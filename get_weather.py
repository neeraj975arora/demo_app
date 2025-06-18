import os
import requests
from dotenv import load_dotenv

def get_weather(city: str) -> str:
    """
    Fetch current weather for a city using OpenWeatherMap API.
    Returns a concise string summary.
    """
    load_dotenv()
    api_key = os.getenv('OPENWEATHER_API_KEY')
    if not api_key:
        return "OpenWeatherMap API key not found. Please set OPENWEATHER_API_KEY in your .env file."
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        weather = data["weather"][0]["description"].capitalize()
        temp = data["main"]["temp"]
        return f"Weather in {city}: {weather}, {temp}°C"
    except Exception as e:
        return f"Could not fetch weather for {city}: {e}" 