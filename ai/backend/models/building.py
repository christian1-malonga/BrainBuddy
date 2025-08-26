# backend/models/building.py
from sqlalchemy import Column, Integer, String, Float, Text
from database import Base

class Building(Base):
    __tablename__ = "buildings"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    type = Column(String(100), nullable=False)  # faculty, facility, dormitory, etc.
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    description = Column(Text)
    floor_count = Column(Integer, default=1)
    image_url = Column(String(500))
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "description": self.description,
            "floor_count": self.floor_count,
            "image_url": self.image_url
        }