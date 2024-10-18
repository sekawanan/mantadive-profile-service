# app/main.py
from fastapi import FastAPI
from app.api.v1.endpoints.diver_profile import api_router as diver_profile_router
from app.api.v1.endpoints.diver_license import api_router as diver_license_router
from app.api.v1.endpoints.diver_gear import api_router as diver_gear_router
from app.api.v1.endpoints.master_license import api_router as master_license_router
from app.api.v1.endpoints.master_dive_preference import api_router as master_dive_pref_router
from app.api.v1.endpoints.master_gear import api_router as master_gear_router
from app.api.v1.endpoints.master_brand import api_router as master_brand_router
from app.api.v1.endpoints.master_gear_brand import api_router as master_gear_brand_router
from app.api.v1.endpoints.master_color import api_router as master_color_router
from app.api.v1.endpoints.master_dive_site import api_router as master_dive_site_router
from app.api.v1.endpoints.master_marine_life import api_router as master_marine_life_router
from app.api.v1.endpoints.dive_preference import api_router as dive_preference_router
from app.api.v1.endpoints.dive_log import api_router as dive_log_router
from app.api.v1.endpoints.master_dive_type import api_router as master_dive_type_router
from app.core.config import settings
from app.database.session import engine, Base
from contextlib import asynccontextmanager
import logging

# Configure logging
# logging.basicConfig(level=logging.INFO)


# Set up logging for SQLAlchemy to show SQL queries
logging.basicConfig(level=logging.INFO)
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    logger.info("Starting up...")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # Shutdown logic
    logger.info("Shutting down...")
    await engine.dispose()

# Create FastAPI instance with lifespan
app = FastAPI(
    title="Diver API",
    version="1.0.0",
    lifespan=lifespan,
    root_path="/api-lab"
)

# Include API routers
app.include_router(diver_profile_router, prefix="/api-lab/v1", tags=["diver-profiles"])
app.include_router(diver_license_router, prefix="/api-lab/v1", tags=["diver-licenses"])
app.include_router(diver_gear_router, prefix="/api-lab/v1", tags=["diver-gears"])
app.include_router(master_license_router, prefix="/api-lab/v1", tags=["master-licenses"])
app.include_router(master_dive_pref_router, prefix="/api-lab/v1", tags=["master-dive-preferences"])
app.include_router(master_gear_router, prefix="/api-lab/v1", tags=["master-gears"])
app.include_router(master_brand_router, prefix="/api-lab/v1", tags=["master-brands"])
app.include_router(master_gear_brand_router, prefix="/api-lab/v1", tags=["master-gears-brands"])
app.include_router(master_color_router, prefix="/api-lab/v1", tags=["master-colors"])
app.include_router(master_dive_site_router, prefix="/api-lab/v1", tags=["master-dive-sites"])
app.include_router(master_marine_life_router, prefix="/api-lab/v1", tags=["master-marine-lifes"])
app.include_router(dive_preference_router, prefix="/api-lab/v1", tags=["dive-preferences"])
app.include_router(master_dive_type_router, prefix="/api-lab/v1", tags=["master-dive-types"])
app.include_router(dive_log_router, prefix="/api-lab/v1", tags=["dive-logs"])