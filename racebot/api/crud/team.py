# crud/team.py
from sqlalchemy.orm import Session
from racebot.models import Team, Driver
from ..schemas.team import TeamCreate

def create_team(db: Session, team_data: TeamCreate):
    team = Team(**team_data.dict())
    db.add(team)
    db.commit()
    db.refresh(team)
    return team

def get_teams_by_server(db: Session, server_id: int):
    return db.query(Team).filter(Team.server_id == server_id).all()

def assign_driver_to_team(db: Session, driver_id: int, team_id: int):
    driver = db.query(Driver).filter(Driver.id == driver_id).first()
    if driver:
        driver.team_id = team_id
        db.commit()
        db.refresh(driver)
    return driver

def get_team_drivers(db: Session, team_id: int):
    return db.query(Driver).filter(Driver.team_id == team_id).all()
