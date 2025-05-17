# schemas/team.py
from pydantic import BaseModel
from typing import List, Optional

class TeamBase(BaseModel):
    name: str
    server_id: int

class TeamCreate(TeamBase):
    pass

class TeamOut(TeamBase):
    id: int

    class Config:
        orm_mode = True

class DriverOut(BaseModel):
    id: int
    name: str
    discord_user_id: str

    class Config:
        orm_mode = True
