import json
import requests


# Adapter class to adapt local weather data to the interface expected by WeatherService
class LocalWeatherAdapter:
    def __init__(self, filename):
        # Initialize adapter with filename for local weather data
        self.filename = filename

    def fetch_weather(self, city):
        # Open local weather data file
        with open(self.filename, 'r') as file:
            # Load weather data from JSON file
            data = json.load(file)
            # Check if data for the requested city exists
            if city in data:
                # If exists, return weather data for the city
                return data[city]
            else:
                # If not exists, return None
                return None


# Interface for the WeatherService class
class WeatherServiceInterface:
    def fetch_weather(self, city):
        pass


# WeatherService class implementing the WeatherServiceInterface
class WeatherService(WeatherServiceInterface):
    def __init__(self, adapter):
        # Initialize WeatherService with adapter
        self.adapter = adapter

    def fetch_weather(self, city):
        # Fetch weather data using adapter
        return self.adapter.fetch_weather(city)


# Decorator class to add additional functionality to the WeatherService
class WeatherServiceDecorator(WeatherServiceInterface):
    def __init__(self, weather_service):
        # Initialize with the weather service to be decorated
        self.weather_service = weather_service

    def fetch_weather(self, city):
        # Fetch weather data using the wrapped weather service
        weather_data = self.weather_service.fetch_weather(city)
        # Add additional functionality (decorating behavior)
        if weather_data:
            weather_data['description'] = f"{weather_data['description']}"
        return weather_data


def main():
    # Prompt user to choose data source
    choice = input("Enter 'api' to fetch data from API or 'file' to fetch data from a local file: ")
    # Check user choice
    if choice == "api":
        # If choice is API, prompt user for city name
        city = input("Enter the city name: ")
        # Create instance of WeatherService with LocalWeatherAdapter for API
        url = f"https://api.weather.com/{city}"
        response = requests.get(url)
        # Check if request was successful
        if response.status_code == 200:
            return response.json()
        else:
            # If request failed, return None
            return None
    elif choice == "file":
        # If choice is file, prompt user for city name
        city = input("Enter the city name: ")
        # Create instance of WeatherService with LocalWeatherAdapter for local file
        adapter = WeatherService(LocalWeatherAdapter("weather_data_local.json"))
    else:
        # If invalid choice, print error message and exit
        print("Invalid choice")
        return

    # Create the WeatherService object
    weather_service = WeatherService(adapter)
    # Decorate the WeatherService object
    decorated_weather_service = WeatherServiceDecorator(weather_service)

    # Fetch weather data for the entered city using the decorated service
    weather_data = decorated_weather_service.fetch_weather(city)
    # Check if weather data was fetched successfully
    if weather_data:
        # If successful, print temperature and decorated description of the city
        print(f"Weather in {city}: {weather_data['temperature']}°C")
        print(f"Description: {weather_data['description']}")
    else:
        # If failed, print error message
        print("Failed to fetch weather data")


if __name__ == "__main__":
    main()
