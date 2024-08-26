# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["RadarEmailSeries"]

class RadarEmailSeries(BaseModel):
    fail: List[str] = FieldInfo(alias = "FAIL")

    none: List[str] = FieldInfo(alias = "NONE")

    pass_: List[str] = FieldInfo(alias = "PASS")