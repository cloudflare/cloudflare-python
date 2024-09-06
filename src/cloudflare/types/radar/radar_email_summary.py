# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["RadarEmailSummary"]


class RadarEmailSummary(BaseModel):
    fail: str = FieldInfo(alias="FAIL")

    none: str = FieldInfo(alias="NONE")

    pass_: str = FieldInfo(alias="PASS")
