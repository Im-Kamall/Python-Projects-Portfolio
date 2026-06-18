city = input("Enter city name: ")

weather_data = {
    "surat": "32°C, Sunny",
    "mumbai": "30°C, Cloudy",
    "delhi": "35°C, Hot"
}

city = city.lower()

if city in weather_data:
    print("Weather in", city, ":", weather_data[city])
else:
    print("Weather data not found.")