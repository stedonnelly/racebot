# -*- coding: utf-8 -*-
# models/team.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Team(Base):
    __tablename__ = "team"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    server_id = Column(Integer, ForeignKey("server.id"), nullable=False)

    server = relationship("Server", back_populates="teams")
    drivers = relationship("Driver", back_populates="team")
