# app/dependencies.py

from app.repositories.diver_license_repository import DiverLicenseRepository
from app.repositories.diver_profile_repository import DiverProfileRepository
from app.repositories.master_license_repository import MasterLicenseRepository
from app.repositories.dive_preference_repository import DivePreferenceRepository
from app.services.diver_license_service import DiverLicenseService
from app.services.diver_profile_service import DiverProfileService
from app.services.master_license_service import MasterLicenseService
from app.services.dive_preference_service import DivePreferenceService
from app.database.session import AsyncSession, get_db
from fastapi import Depends

# Repository dependencies
def get_diver_license_repository(db: AsyncSession = Depends(get_db)) -> DiverLicenseRepository:
    return DiverLicenseRepository(db)

def get_diver_profile_repository(db: AsyncSession = Depends(get_db)) -> DiverProfileRepository:
    return DiverProfileRepository(db)

def get_master_license_repository(db: AsyncSession = Depends(get_db)) -> MasterLicenseRepository:
    return MasterLicenseRepository(db)

def get_dive_preference_repository(db: AsyncSession = Depends(get_db)) -> DivePreferenceRepository:
    return DivePreferenceRepository(db)

# Service dependencies
def get_diver_license_service(
    license_repo: DiverLicenseRepository = Depends(get_diver_license_repository),
    profile_repo: DiverProfileRepository = Depends(get_diver_profile_repository),
    master_license_repo: MasterLicenseRepository = Depends(get_master_license_repository)
) -> DiverLicenseService:
    return DiverLicenseService(
        license_repository=license_repo,
        profile_repository=profile_repo,
        master_license_repository=master_license_repo
    )

def get_diver_profile_service(
    repository: DiverProfileRepository = Depends(get_diver_profile_repository)
) -> DiverProfileService:
    return DiverProfileService(repository)

def get_master_license_service(
    master_license_repo: MasterLicenseRepository = Depends(get_master_license_repository)
) -> MasterLicenseService:
    return MasterLicenseService(master_license_repository=master_license_repo)

def get_dive_preference_service(
    dive_pref_repo: DivePreferenceRepository = Depends(get_dive_preference_repository)
) -> DivePreferenceService:
    return DivePreferenceService(dive_preference_repository=dive_pref_repo)