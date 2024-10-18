# app/api/v1/endpoints/diver_profile.py
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from app.schemas import (
    DiverProfileCreate,
    DiverProfileRead,
    DiverProfileUpdate,
    DiverInfoResponse,
    DiverInfoData,
    DiverGearRead,
    DiverLicenseRead,
    DivePreferenceRead
)
from app.services.diver_profile_service import DiverProfileService
from app.dependencies import get_diver_profile_service

api_router = APIRouter()

@api_router.post("/diver-profiles", response_model=DiverProfileRead, status_code=status.HTTP_201_CREATED)
async def create_diver_profile(
    diver_profile: DiverProfileCreate,
    service: DiverProfileService = Depends(get_diver_profile_service)
):
    created_profile = await service.create_diver_profile(diver_profile)
    return DiverProfileRead.from_orm(created_profile)

@api_router.get("/diver-profiles", response_model=List[DiverProfileRead])
async def read_diver_profiles(service: DiverProfileService = Depends(get_diver_profile_service)):
    profiles = await service.get_all_diver_profiles()
    return [DiverProfileRead.from_orm(profile) for profile in profiles]

@api_router.get("/diver-profiles/{diver_profile_id}", response_model=DiverProfileRead)
async def read_diver_profile(
    diver_profile_id: int,
    service: DiverProfileService = Depends(get_diver_profile_service)
):
    profile = await service.get_diver_profile(diver_profile_id)
    if not profile:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Diver profile not found")
    return DiverProfileRead.from_orm(profile)

@api_router.put("/diver-profiles/{diver_profile_id}", response_model=DiverProfileRead)
async def update_diver_profile(
    diver_profile_id: int,
    diver_profile: DiverProfileUpdate,
    service: DiverProfileService = Depends(get_diver_profile_service)
):
    updated_profile = await service.update_diver_profile(diver_profile_id, diver_profile)
    if not updated_profile:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Diver profile not found")
    return DiverProfileRead.from_orm(updated_profile)

@api_router.delete("/diver-profiles/{diver_profile_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_diver_profile(
    diver_profile_id: int,
    service: DiverProfileService = Depends(get_diver_profile_service)
):
    success = await service.delete_diver_profile(diver_profile_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Diver profile not found")
    return

# New route for nested JSON response
@api_router.get("/diver-profiles/{diver_profile_id}/info", response_model=DiverInfoResponse)
async def get_diver_profile_info(
    diver_profile_id: int,
    service: DiverProfileService = Depends(get_diver_profile_service)
):
    profile = await service.get_diver_profile(diver_profile_id)
    if not profile:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Diver profile not found")
    
    # Construct DiverInfoData using from_orm for nested relationships
    data = DiverInfoData(
        profile=DiverProfileRead.from_orm(profile),
        licenses=[DiverLicenseRead.from_orm(license) for license in profile.diver_licenses],
        dive_preferences=[DivePreferenceRead.from_orm(pref) for pref in profile.dive_preferences],
        diver_gears=[DiverGearRead.from_orm(gear) for gear in profile.diver_gears]
    )
    
    # Construct and return the response
    response = DiverInfoResponse(
        status="success",
        message="Diver info fetched successfully",
        data=data
    )
    return response