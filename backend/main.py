from flask import request, jsonify
from config import app, db
from models import Weather_entry
from location_service import LocationService
from open_weather_api import WeatherAPI
from datetime import datetime

@app.route("/weather_entries", methods=["GET"])
def get_weather_entry():
    weather_entries = Weather_entry.query.all()
    json_entries = list(map(lambda x: x.to_json(), weather_entries))

    sorted_entries = sorted(
        json_entries,
        key=lambda entry: datetime.strptime(entry["time"], "%d/%m/%Y %I:%M:%S %p"),
        reverse=True
    )
    return jsonify({"weatherEntries": sorted_entries})

@app.route("/new_weather_entry", methods=["POST"])
def get_new_weather_entry():
    country = request.json.get("country")
    city = request.json.get("city")

    if not city and not country:
        return (jsonify({"message":"No location entered"}), 400)
    elif not city:
        return (jsonify({"message":"City location is required"}), 400)
    elif not country:
        return (jsonify({"message":"Country location is required"}), 400)

    #Instantiate LocationService to get coordinates and check if the location is valid
    location_service = LocationService()
    coordinates = location_service.get_coordinates(city, country)
    if not coordinates:
        return (jsonify({"message":"Invalid location entered"}), 400)
    
    two_letter_code = location_service.get_country_code(country)
    if two_letter_code:
        country = two_letter_code
    
    #Get API key from text file
    with open('openWeatherAPIKey.txt', 'r') as file: api_key = file.read()

    #Instatiate open weather api to get the desired weather conditions
    weather_api = WeatherAPI(api_key)
    latitude, longitude = coordinates
    weather_data = weather_api.get_weather_by_coordinates(latitude, longitude)

    #Process and store weather data in database
    description = weather_data['weather'][0]['description']
    temperature_min = weather_data['main']['temp_min']
    temperature_max = weather_data['main']['temp_max']
    humidity = weather_data['main']['humidity']
    time = datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")

    new_weather_entry = Weather_entry(
        country = country,
        city = city,
        description = description,
        temperature_min = temperature_min,
        temperature_max = temperature_max,
        humidity = humidity,
        time = time
    )
    try:
        db.session.add(new_weather_entry)
        db.session.commit()
    except Exception as e:
        return (jsonify({"message":str(e)}), 400)
    
    return (jsonify({
                    "country": country,
                    "city": city,
                    "description": description,
                    "temperatureMin": temperature_min,
                    "temperatureMax": temperature_max,
                    "humidity": humidity,
                    "time": time
                     }), 201)

@app.route("/delete_weather_entry/<int:entry_id>", methods=["DELETE"])
def delete_weather_entry(entry_id):
    weather_entry = Weather_entry.query.get(entry_id)
    if not weather_entry:
        return (jsonify({"message":"Entry not found"}), 404)
    
    db.session.delete(weather_entry)
    db.session.commit()
    return (jsonify({"message":"Entry deleted"}), 200)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000, debug=True)