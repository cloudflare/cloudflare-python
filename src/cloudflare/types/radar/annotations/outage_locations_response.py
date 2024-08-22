# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["OutageLocationsResponse", "Annotation"]

class Annotation(BaseModel):
    client_country_alpha2: str = FieldInfo(alias = "clientCountryAlpha2")

    client_country_name: str = FieldInfo(alias = "clientCountryName")

    value: str

class OutageLocationsResponse(BaseModel):
    annotations: List[Annotation]