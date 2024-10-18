# app/schemas/master_dive_preference.py
from pydantic import BaseModel
from datetime import datetime

class MasterDivePreferenceBase(BaseModel):
    label: str

class MasterDivePreferenceCreate(MasterDivePreferenceBase):
    label: str
    # pass

class MasterDivePreferenceRead(MasterDivePreferenceBase):
    id: int
    label: str
    created_at: datetime
    modified_at: datetime

    class Config:
        from_attributes = True