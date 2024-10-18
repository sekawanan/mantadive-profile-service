# app/models/diver_gear.py
from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from app.database.session import Base
from sqlalchemy.orm import relationship
from datetime import datetime

class DiverGear(Base):
    __tablename__ = "diver_gears"

    id = Column(Integer, primary_key=True, index=True)
    diver_profile_id = Column(Integer, ForeignKey("diver_profiles.id"), nullable=False)
    master_gears_brand_id = Column(Integer, ForeignKey("master_gears_brands.id"), nullable=False)
    master_color_id = Column(Integer, ForeignKey("master_colors.id"), nullable=False)
    type = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    modified_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    diver_profile = relationship("DiverProfile", back_populates="diver_gears")
    master_gears_brands = relationship("MasterGearBrand", back_populates="diver_gears")
    master_colors = relationship("MasterColor", back_populates="diver_gears")

    # @property
    # def color_label(self):
    #     return self.master_colors.label if self.master_colors else None