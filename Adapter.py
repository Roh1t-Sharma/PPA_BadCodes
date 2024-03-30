import requests

class WeatherService:
    def fetch_weather(self, city):
        # Construct URL for fetching weather data
        url = f"https://api.weather.com/{city}"
        # Make HTTP GET request to the weather API
        response = requests.get(url)
        # Check if request was successful
        if response.status_code == 200:
            # If successful, return weather data in JSON format
            return response.json()
        else:
            # If request failed, return None
            return None

def main():
    # Prompt user to enter city name
    city = input("Enter the city name: ")
    # Create instance of WeatherService
    weather_service = WeatherService()
    # Fetch weather data for the entered city
    weather_data = weather_service.fetch_weather(city)
    # Check if weather data was fetched successfully
    if weather_data:
        # If successful, print temperature of the city
        print(f"Weather in {city}: {weather_data['temperature']}°C")
    else:
        # If failed, print error message
        print("Failed to fetch weather data")

if __name__ == "__main__":
    main()
