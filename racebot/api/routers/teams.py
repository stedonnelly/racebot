# routers/teams.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from racebot.db.db import get_db
from ..schemas.team import TeamCreate, TeamOut, DriverOut
from ..crud import team as crud

router = APIRouter()

@router.post("/", response_model=TeamOut)
def create_team(team: TeamCreate, db: Session = Depends(get_db)):
    return crud.create_team(db, team)

@router.get("/server/{server_id}", response_model=list[TeamOut])
def list_teams(server_id: int, db: Session = Depends(get_db)):
    return crud.get_teams_by_server(db, server_id)

@router.post("/{team_id}/assign-driver", response_model=DriverOut)
def assign_driver(team_id: int, driver_id: int, db: Session = Depends(get_db)):
    driver = crud.assign_driver_to_team(db, driver_id, team_id)
    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found")
    return driver

@router.get("/{team_id}/drivers", response_model=list[DriverOut])
def get_drivers_on_team(team_id: int, db: Session = Depends(get_db)):
    return crud.get_team_drivers(db, team_id)
