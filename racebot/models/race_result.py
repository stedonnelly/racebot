# -*- coding: utf-8 -*-
# models/race_result.py

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class RaceResult(Base):
    __tablename__ = "race_result"

    id = Column(Integer, primary_key=True)
    race_id = Column(Integer, ForeignKey("race.id"), nullable=False)
    driver_id = Column(Integer, ForeignKey("driver.id"), nullable=False)
    position = Column(Integer)
    points = Column(Integer)

    race = relationship("Race", back_populates="results")
    driver = relationship("Driver", back_populates="results")
