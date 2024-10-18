# app/models/master_gear_brand.py
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from app.database.session import Base
from sqlalchemy.orm import relationship
from datetime import datetime

class MasterGearBrand(Base):
    __tablename__ = "master_gears_brands"

    id = Column(Integer, primary_key=True, index=True)
    master_gear_id = Column(Integer, ForeignKey("master_gears.id"), nullable=False)
    master_brand_id = Column(Integer, ForeignKey("master_brands.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    modified_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    diver_gears = relationship("DiverGear", back_populates="master_gears_brands")
    master_gears = relationship("MasterGear", back_populates="master_gears_brands")
    master_brands = relationship("MasterBrand", back_populates="master_gears_brands")

    # @property
    # def gear_label(self):
    #     return self.master_gears.label if self.master_gears else None
    
    # @property
    # def brand_label(self):
    #     return self.master_brands.label if self.master_brands else None