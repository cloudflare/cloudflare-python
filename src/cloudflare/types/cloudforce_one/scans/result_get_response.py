# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .scan_result import ScanResult

__all__ = ["ResultGetResponse"]


class ResultGetResponse(BaseModel):
    one_one_one_one: List[ScanResult] = FieldInfo(alias="1.1.1.1")
