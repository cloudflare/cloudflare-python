# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....._models import BaseModel

from typing import List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["TimeseriesGroupMaliciousResponse", "Serie0"]

class Serie0(BaseModel):
    malicious: List[str] = FieldInfo(alias = "MALICIOUS")

    not_malicious: List[str] = FieldInfo(alias = "NOT_MALICIOUS")

class TimeseriesGroupMaliciousResponse(BaseModel):
    meta: object

    serie_0: Serie0