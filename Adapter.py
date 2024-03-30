import json

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

def main():
    # Prompt user to choose data source
    choice = input("Enter 'api' to fetch data from API or 'file' to fetch data from a local file: ")
    # Check user choice
    if choice == "api":
        # If choice is API, prompt user for city name
        city = input("Enter the city name: ")
        # Create instance of WeatherService with LocalWeatherAdapter for API
        adapter = WeatherService(LocalWeatherAdapter("weather_data.json"))
    elif choice == "file":
        # If choice is file, prompt user for city name
        city = input("Enter the city name: ")
        # Create instance of WeatherService with LocalWeatherAdapter for local file
        adapter = WeatherService(LocalWeatherAdapter("weather_data_local.json"))
    else:
        # If invalid choice, print error message and exit
        print("Invalid choice")
        return

    # Fetch weather data for the entered city using the chosen adapter
    weather_data = adapter.fetch_weather(city)
    # Check if weather data was fetched successfully
    if weather_data:
        # If successful, print temperature of the city
        print(f"Weather in {city}: {weather_data['temperature']}°C")
    else:
        # If failed, print error message
        print("Failed to fetch weather data")

if __name__ == "__main__":
    main()
