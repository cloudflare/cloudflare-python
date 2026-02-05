# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["GeolocationGetResponse", "Geolocation", "GeolocationParent", "GeolocationParentParent"]


class GeolocationParentParent(BaseModel):
    geo_id: str = FieldInfo(alias="geoId")

    latitude: str
    """A numeric string."""

    longitude: str
    """A numeric string."""

    name: str

    type: Literal["CONTINENT", "COUNTRY", "ADM1"]
    """The type of the geolocation."""


class GeolocationParent(BaseModel):
    geo_id: str = FieldInfo(alias="geoId")

    latitude: str
    """A numeric string."""

    longitude: str
    """A numeric string."""

    name: str

    parent: GeolocationParentParent

    type: Literal["CONTINENT", "COUNTRY", "ADM1"]
    """The type of the geolocation."""


class Geolocation(BaseModel):
    geo_id: str = FieldInfo(alias="geoId")

    latitude: str
    """A numeric string."""

    longitude: str
    """A numeric string."""

    name: str

    parent: GeolocationParent

    type: Literal["CONTINENT", "COUNTRY", "ADM1"]
    """The type of the geolocation."""


class GeolocationGetResponse(BaseModel):
    geolocation: Geolocation
