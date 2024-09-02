# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["LocationListResponse", "Location"]


class Location(BaseModel):
    alpha2: str

    latitude: str

    longitude: str

    name: str


class LocationListResponse(BaseModel):
    locations: List[Location]
