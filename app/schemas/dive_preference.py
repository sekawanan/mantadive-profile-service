# app/schemas/dive_preference.py
from __future__ import annotations  # Add this line at the very top
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Base schema
class DivePreferenceBase(BaseModel):
    diver_profile_id: int
    master_dive_preference_id: int

class DivePreferenceCreate(DivePreferenceBase):
    pass

class DivePreferenceUpdate(BaseModel):
    diver_profile_id: Optional[int]
    master_dive_preference_id: Optional[int]

class DivePreferenceRead(BaseModel):
    id: int
    diver_profile_id: int
    master_dive_preference_id: int
    label: Optional[str]  # Assuming label is fetched via relationship
    created_at: datetime
    modified_at: datetime

    class Config:
       from_attributes=True  # Important to serialize SQLAlchemy models