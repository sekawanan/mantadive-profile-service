# app/repositories/dive_preference_repository.py
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload

from app.models.dive_preference import DivePreference

class DivePreferenceRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_preferences_by_diver(self, diver_profile_id: int) -> List[DivePreference]:
        result = await self.db.execute(
            select(DivePreference)
            .options(selectinload(DivePreference.master_preference))
            .where(DivePreference.diver_profile_id == diver_profile_id)
        )
        preferences = result.scalars().all()
        return preferences

    async def create_preference(self, preference: DivePreference) -> DivePreference:
        self.db.add(preference)
        await self.db.commit()
        await self.db.refresh(preference)
        return preference