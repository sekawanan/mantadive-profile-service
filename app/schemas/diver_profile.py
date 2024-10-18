# app/schemas/diver_profile.py
from __future__ import annotations  # Add this line at the very top
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime, date

# Import necessary schemas
from .diver_license import DiverLicenseRead
from .dive_preference import DivePreferenceRead
from .diver_gear import DiverGearRead

class DiverProfileBase(BaseModel):
    user_id: int
    first_name: str
    last_name: str
    full_name: str
    birth_date: date

class DiverProfileCreate(DiverProfileBase):
    """
    Schema for creating a new diver profile.
    """
    user_id: int
    first_name: Optional[str]
    last_name: Optional[str]
    full_name: str
    birth_date: date
    
    class Config:
        from_attributes = True

class DiverProfileUpdate(BaseModel):
    user_id: Optional[int] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None

class DiverProfileRead(DiverProfileBase):
    id: int
    created_at: datetime
    modified_at: datetime
    licenses: List[DiverLicenseRead] = []
    dive_preferences: List[DivePreferenceRead] = []
    diver_gears: List[DiverGearRead] = []  # Ensure DiverGearRead is defined

    class Config:
        from_attributes = True  # Enables from_orm
        populate_by_name = True  # Pydantic V2: replaces allow_population_by_field_name