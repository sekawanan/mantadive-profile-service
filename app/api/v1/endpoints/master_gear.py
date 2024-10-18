# app/api/v1/endpoints/master_license.py
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.master_gear import MasterGearRead
from app.services.master_gear_service import MasterGearService
from app.repositories.master_gear_repository import MasterGearRepository
from app.database.session import get_db

api_router = APIRouter()

@api_router.get("/master-gears", response_model=List[MasterGearRead])
async def read_master_gears(db: AsyncSession = Depends(get_db)):
    repository = MasterGearRepository(db)
    service = MasterGearService(repository)
    licenses = await service.get_all_master_gears
    return licenses