# app/models/dive_preference.py
from sqlalchemy import Column, Integer, ForeignKey, DateTime
from app.database.session import Base
from sqlalchemy.orm import relationship
from datetime import datetime

class DivePreference(Base):
    __tablename__ = "dive_preferences"

    id = Column(Integer, primary_key=True, index=True)
    diver_profile_id = Column(Integer, ForeignKey("diver_profiles.id"), nullable=False)
    master_dive_preference_id = Column(Integer, ForeignKey("master_dive_preferences.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    modified_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    diver_profile = relationship("DiverProfile", back_populates="dive_preferences")
    master_preference = relationship("MasterDivePreference", back_populates="dive_preferences")

    @property
    def label(self):
        return self.master_preference.label if self.master_preference else None