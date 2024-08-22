# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["TimeseriesGroupDNSSECResponse", "Serie0"]

class Serie0(BaseModel):
    insecure: List[str] = FieldInfo(alias = "INSECURE")

    invalid: List[str] = FieldInfo(alias = "INVALID")

    other: List[str] = FieldInfo(alias = "OTHER")

    secure: List[str] = FieldInfo(alias = "SECURE")

class TimeseriesGroupDNSSECResponse(BaseModel):
    meta: object

    serie_0: Serie0