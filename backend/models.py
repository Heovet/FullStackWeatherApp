from config import db

class Weather_entry(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    country = db.Column(db.String(2), nullable=False)
    city = db.Column(db.String(168), nullable=False)
    description = db.Column(db.String(40), nullable=False)
    temperature_min = db.Column(db.Float, nullable=True)
    temperature_max = db.Column(db.Float, nullable=True)
    humidity = db.Column(db.Float, nullable=True)
    time = db.Column(db.String(22), nullable=False)

    def to_json(self):
        return{
            "id": self.id,
            "country": self.country,
            "city": self.city,
            "description": self.description,
            "temperatureMin": self.temperature_min,
            "temperatureMax": self.temperature_max,
            "humidity": self.humidity,
            "time": self.time
        }
