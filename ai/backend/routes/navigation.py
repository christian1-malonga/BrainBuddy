# backend/routes/navigation.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.building import Building
from typing import List

router = APIRouter(prefix="/api/navigation", tags=["navigation"])

@router.get("/buildings", response_model=List[dict])
async def get_all_buildings(db: Session = Depends(get_db)):
    """Get all university buildings"""
    buildings = db.query(Building).all()
    return [building.to_dict() for building in buildings]

@router.get("/buildings/{building_id}")
async def get_building(building_id: int, db: Session = Depends(get_db)):
    """Get specific building details"""
    building = db.query(Building).filter(Building.id == building_id).first()
    if not building:
        raise HTTPException(status_code=404, detail="Building not found")
    return building.to_dict()

@router.post("/buildings")
async def create_building(building_data: dict, db: Session = Depends(get_db)):
    """Create new building (Admin only)"""
    building = Building(**building_data)
    db.add(building)
    db.commit()
    db.refresh(building)
    return building.to_dict()

@router.put("/buildings/{building_id}")
async def update_building(building_id: int, building_data: dict, db: Session = Depends(get_db)):
    """Update building information (Admin only)"""
    building = db.query(Building).filter(Building.id == building_id).first()
    if not building:
        raise HTTPException(status_code=404, detail="Building not found")
    
    for key, value in building_data.items():
        setattr(building, key, value)
    
    db.commit()
    return building.to_dict()