# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["LocationGetResponse", "Location"]


class Location(BaseModel):
    alpha2: str

    confidence_level: int = FieldInfo(alias="confidenceLevel")

    latitude: str

    longitude: str

    name: str

    region: str

    subregion: str


class LocationGetResponse(BaseModel):
    location: Location
