# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["ScanResult"]


class ScanResult(BaseModel):
    number: Optional[float] = None

    proto: Optional[str] = None

    status: Optional[str] = None
