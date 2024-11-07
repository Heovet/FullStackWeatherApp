import pycountry
from geopy.geocoders import Nominatim

class LocationService:
    def __init__(self):
        self.geolocator = Nominatim(user_agent="geoapi")
    
    def get_coordinates(self, city, country=None):
        location_query = f"{city}, {country}" if country else city
        location = self.geolocator.geocode(location_query)
        if location:
            return location.latitude, location.longitude
        else:
            raise ValueError("Location not found. Please try with a different city or country.")
        
    def get_country_code(self, country_name):
        try:
            # Normalize the country name to match pycountry's naming conventions
            country = pycountry.countries.lookup(country_name)
            return country.alpha_2  # Get the two-letter country code
        except LookupError:
            return None  # Return None if the country is not found

def test_case():
    # city = input("Enter the city name: ")
    # country = input("Enter the country name (optional, press Enter to skip): ").strip() or None
    
    city = "London"
    country = "UK"

    location_service = LocationService()
    try:
        country_code = location_service.get_country_code(country)
        print(country_code)
        latitude, longitude = location_service.get_coordinates(city, country)
        print(f"Coordinates for {city}, {country if country else ''}:")
        print(f"Latitude: {latitude}, Longitude: {longitude}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    test_case()
