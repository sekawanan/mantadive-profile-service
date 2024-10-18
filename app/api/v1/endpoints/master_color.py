# app/api/v1/endpoints/master_color.py
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.master_color import MasterColorRead
from app.repositories.master_color_repository import MasterColorRepository
from app.services.master_color_service import MasterColorService
from app.database.session import get_db

api_router = APIRouter()

@api_router.get("/master-colors", response_model=List[MasterColorRead])
async def read_master_colors(db: AsyncSession = Depends(get_db)):
    repository = MasterColorRepository(db)
    service = MasterColorService(repository)
    colors = await service.get_all_master_colors()
    return colors