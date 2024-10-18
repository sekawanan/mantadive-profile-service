# app/models/master_gear.py
from sqlalchemy import Column, Integer, String, DateTime
from app.database.session import Base
from sqlalchemy.orm import relationship
from datetime import datetime

class MasterGear(Base):
    __tablename__ = "master_gears"

    id = Column(Integer, primary_key=True, index=True)
    label = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    modified_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    master_gears_brands = relationship("MasterGearBrand", back_populates="master_gears")
    # diver_gears = relationship("DiverGear", back_populates="master_gear")