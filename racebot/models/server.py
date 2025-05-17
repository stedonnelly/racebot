# -*- coding: utf-8 -*-
# models/server.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Server(Base):
    __tablename__ = "server"

    id = Column(Integer, primary_key=True)
    discord_guild_id = Column(String(64), unique=True, nullable=False)
    name = Column(String(255))

    teams = relationship("Team", back_populates="server", cascade="all, delete-orphan")
    drivers = relationship("Driver", back_populates="server", cascade="all, delete-orphan")
    tiers = relationship("Tier", back_populates="server", cascade="all, delete-orphan")
    races = relationship("Race", back_populates="server", cascade="all, delete-orphan")