# app/schemas/diver_gear.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Base schema
class DiverGearBase(BaseModel):
    diver_profile_id: int
    master_gears_brand_id: int
    master_color_id: int
    type: str

# Create schema
class DiverGearCreate(DiverGearBase):
    pass

# Update schema
class DiverGearUpdate(BaseModel):
    diver_profile_id: Optional[int]
    master_gears_brand_id: Optional[int]
    master_color_id: Optional[int]
    type: Optional[str]

# Read schema
class DiverGearRead(DiverGearBase):
    id: int
    color_label: Optional[str]
    gear_label: Optional[str]
    brand_label: Optional[str]
    created_at: datetime
    modified_at: datetime

    class Config:
        from_attributes=True