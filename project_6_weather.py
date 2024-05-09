import requests
from geopy.geocoders import Nominatim


def get_weather(city):

    locator = Nominatim(user_agent="weather_app")

    location = locator.geocode(city)

    if location:
        latitude, longitude = location.latitude, location.longitude
        url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            weather = data['current']
            temp = weather['temperature_2m']
            wind_speed = weather['wind_speed_10m']
            time = weather['time']

            print("Complete Address:", location.address)
            print(f'Current Temperature in : {temp} °C')
            print(f'Current Wind Speed in : {wind_speed} km/h')
            print(f"Time: {time}")

        else:
            print("Error fetching weather data. Please try again.")
    else:
        print("Location not found.")


city_name = input("Enter the name of country, city or village: ")
get_weather(city_name)
