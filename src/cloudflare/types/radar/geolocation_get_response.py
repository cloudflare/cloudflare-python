# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
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

    code: Optional[str] = None

    locale: Optional[str] = None
    """BCP 47 locale code used for the geolocation name translation"""


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

    code: Optional[str] = None

    locale: Optional[str] = None
    """BCP 47 locale code used for the geolocation name translation"""


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

    code: Optional[str] = None

    locale: Optional[str] = None
    """BCP 47 locale code used for the geolocation name translation"""


class GeolocationGetResponse(BaseModel):
    geolocation: Geolocation
