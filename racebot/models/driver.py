# -*- coding: utf-8 -*-
# models/driver.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Driver(Base):
    __tablename__ = "driver"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    discord_user_id = Column(String)
    server_id = Column(Integer, ForeignKey("server.id"), nullable=False)
    team_id = Column(Integer, ForeignKey("team.id"), nullable=True)

    server = relationship("Server", back_populates="drivers")
    team = relationship("Team", back_populates="drivers")
    results = relationship("RaceResult", back_populates="driver")
