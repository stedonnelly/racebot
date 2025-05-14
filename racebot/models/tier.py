# -*- coding: utf-8 -*-
# models/tier.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Tier(Base):
    __tablename__ = "tier"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    server_id = Column(Integer, ForeignKey("server.id"), nullable=False)

    server = relationship("Server", back_populates="tiers")
    races = relationship("Race", back_populates="tier")
