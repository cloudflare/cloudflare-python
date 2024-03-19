# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel

__all__ = ["LocationListResponse", "Location"]


class Location(BaseModel):
    alpha2: str

    latitude: str

    longitude: str

    name: str


class LocationListResponse(BaseModel):
    locations: List[Location]
