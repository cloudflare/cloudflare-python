# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ColoListResponse"]


class ColoListResponse(BaseModel):
    airport_code: str = FieldInfo(alias="airportCode")
    """Airport code"""

    city: str
    """City"""

    country_code: str = FieldInfo(alias="countryCode")
    """Country code"""
