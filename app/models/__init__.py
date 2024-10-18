# app/models/__init__.py
from .diver_profile import DiverProfile
from .diver_license import DiverLicense
from .diver_gear import DiverGear
from .master_license import MasterLicense
from .master_dive_preference import MasterDivePreference
from .master_gear import MasterGear
from .master_brand import MasterBrand
from .master_gear_brand import MasterGearBrand
from .master_dive_site import MasterDiveSite
from .master_marine_life import MasterMarineLife
from .master_color import MasterColor
from .dive_preference import DivePreference
from .master_dive_type import MasterDiveType
from .dive_log import DiveLog
from .diver_additional_data import DiverAdditionalData


# __all__ = [
#     "DiverProfile",
#     "DiverLicense",
#     "MasterLicense",
#     "MasterDivePreference",
#     "DivePreference",
# ]