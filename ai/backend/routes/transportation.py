# backend/routes/transportation.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.transportation import BusRoute
from datetime import datetime, time

router = APIRouter(prefix="/api/transportation", tags=["transportation"])

@router.get("/routes")
async def get_bus_routes(is_vacation: bool = False, db: Session = Depends(get_db)):
    """Get all bus routes based on schedule type"""
    routes = db.query(BusRoute).filter(BusRoute.is_vacation_schedule == is_vacation).all()
    return [route.to_dict() for route in routes]

@router.get("/routes/{destination}")
async def get_route_details(destination: str, is_vacation: bool = False, db: Session = Depends(get_db)):
    """Get specific route details"""
    route = db.query(BusRoute).filter(
        BusRoute.destination == destination,
        BusRoute.is_vacation_schedule == is_vacation
    ).first()
    
    if not route:
        return {"error": "Route not found"}
    
    return route.to_dict()

@router.get("/next-departure/{destination}")
async def get_next_departure(destination: str, is_vacation: bool = False, db: Session = Depends(get_db)):
    """Get next departure time for a destination"""
    route = db.query(BusRoute).filter(
        BusRoute.destination == destination,
        BusRoute.is_vacation_schedule == is_vacation
    ).first()
    
    if not route:
        return {"error": "Route not found"}
    
    import json
    departure_times = json.loads(route.departure_times)
    current_time = datetime.now().time()
    
    for departure_str in departure_times:
        departure_time = datetime.strptime(departure_str, "%H:%M").time()
        if departure_time > current_time:
            return {"next_departure": departure_str}
    
    # If no more departures today, return first departure of next day
    return {"next_departure": departure_times[0] if departure_times else None}