# racebot/api/routers/drivers.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from racebot.db.db import get_db
from racebot.models import Driver
from racebot.api.schemas.driver import DriverCreate, DriverOut

router = APIRouter()

@router.post("/", response_model=DriverOut)
def create_driver(driver: DriverCreate, db: Session = Depends(get_db)):
    existing = db.query(Driver).filter(
        Driver.discord_user_id == driver.discord_user_id,
        Driver.server_id == driver.server_id
    ).first()
    if existing:
        return existing

    new_driver = Driver(
        name=driver.name,
        discord_user_id=driver.discord_user_id,
        server_id=driver.server_id,
        team_id=driver.team_id
    )
    db.add(new_driver)
    db.commit()
    db.refresh(new_driver)
    return new_driver

@router.get("/server/{server_id}", response_model=list[DriverOut])
def list_drivers(server_id: int, db: Session = Depends(get_db)):
    return db.query(Driver).filter(Driver.server_id == server_id).all()
