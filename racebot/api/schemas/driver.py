from pydantic import BaseModel
from typing import Optional

class DriverCreate(BaseModel):
    name: str
    discord_user_id: str
    server_id: int
    team_id: Optional[int] = None

class DriverOut(DriverCreate):
    id: int

    class Config:
        orm_mode = True
