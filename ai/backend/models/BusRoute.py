from flask_sqlalchemy import SQLAlchemy
from models.user import db
import json

class BusRoute(db.Model):
    __tablename__ = 'bus_routes'
    
    id = db.Column(db.Integer, primary_key=True)
    destination = db.Column(db.String(100), nullable=False)
    route_type = db.Column(db.String(50), nullable=False)  # capital, outside
    is_vacation_schedule = db.Column(db.Boolean, default=False)
    departure_times = db.Column(db.Text)  # JSON string of times
    stops = db.Column(db.Text)  # JSON string of stops
    estimated_duration = db.Column(db.Integer)  # in minutes
    price = db.Column(db.String(20))  # ticket price
    
    def to_dict(self):
        return {
            "id": self.id,
            "destination": self.destination,
            "route_type": self.route_type,
            "is_vacation_schedule": self.is_vacation_schedule,
            "departure_times": json.loads(self.departure_times) if self.departure_times else [],
            "stops": json.loads(self.stops) if self.stops else [],
            "estimated_duration": self.estimated_duration,
            "price": self.price
        }