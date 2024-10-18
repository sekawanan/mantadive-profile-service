# app/api/v1/endpoints/diver_preference.py
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.dive_preference import DivePreferenceRead
from app.services.dive_preference_service import DivePreferenceService
from app.repositories.dive_preference_repository import DivePreferenceRepository
from app.database.session import get_db

api_router = APIRouter()

@api_router.get("/dive-preferences/{diver_profile_id}", response_model=DivePreferenceRead)
async def read_diver_preference(
    diver_profile_id: int,
    db: AsyncSession = Depends(get_db)
):
    repository = DivePreferenceRepository(db)
    service = DivePreferenceService(repository)
    preferences = await service.get_preferences_by_diver(diver_profile_id)
    return preferences
