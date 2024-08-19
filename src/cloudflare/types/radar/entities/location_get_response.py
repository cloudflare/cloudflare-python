# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from pydantic import Field as FieldInfo

from ...._models import BaseModel

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
