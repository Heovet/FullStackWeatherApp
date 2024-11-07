import requests

class WeatherAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    def get_weather_by_coordinates(self, latitude, longitude):
        params = {
            'lat': latitude,
            'lon': longitude,
            'appid': self.api_key,
            'units': 'metric'  # To get the temperature in Celsius
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

def test_case():
    api_key = input("Enter your OpenWeather API key: ")
    latitude = float(input("Enter latitude: "))
    longitude = float(input("Enter longitude: "))
    
    weather_api = WeatherAPI(api_key)
    try:
        weather_data = weather_api.get_weather_by_coordinates(latitude, longitude)
        print("Weather Data:")
        print(weather_data)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    test_case()
