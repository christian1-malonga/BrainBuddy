# backend/models/transportation.py
from sqlalchemy import Column, Integer, String, Time, Boolean, Text
from database import Base

class BusRoute(Base):
    __tablename__ = "bus_routes"
    
    id = Column(Integer, primary_key=True, index=True)
    destination = Column(String(100), nullable=False)
    route_type = Column(String(50), nullable=False)  # capital, outside
    is_vacation_schedule = Column(Boolean, default=False)
    departure_times = Column(Text)  # JSON string of times
    stops = Column(Text)  # JSON string of stops
    estimated_duration = Column(Integer)  # in minutes
    
    def to_dict(self):
        import json
        return {
            "id": self.id,
            "destination": self.destination,
            "route_type": self.route_type,
            "is_vacation_schedule": self.is_vacation_schedule,
            "departure_times": json.loads(self.departure_times) if self.departure_times else [],
            "stops": json.loads(self.stops) if self.stops else [],
            "estimated_duration": self.estimated_duration
        }