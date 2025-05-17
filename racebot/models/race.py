# -*- coding: utf-8 -*-
# models/race.py

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .base import Base
import datetime

class Race(Base):
    __tablename__ = "race"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    date = Column(DateTime, default=datetime.datetime.utcnow)
    server_id = Column(Integer, ForeignKey("server.id"), nullable=False)
    tier_id = Column(Integer, ForeignKey("tier.id"), nullable=True)

    server = relationship("Server", back_populates="races")
    tier = relationship("Tier", back_populates="races")
    results = relationship("RaceResult", back_populates="race")
