# app/services/dive_preference_service.py
from typing import List
from app.repositories.dive_preference_repository import DivePreferenceRepository
from app.models.dive_preference import DivePreference

class DivePreferenceService:
    def __init__(self, repository: DivePreferenceRepository):
        self.repository = repository

    async def get_preferences_by_diver(self, diver_profile_id: int) -> List[DivePreference]:
        return await self.repository.get_preferences_by_diver(diver_profile_id)

    async def create_preference(self, preference_data: DivePreference) -> DivePreference:
        return await self.repository.create_preference(preference_data)