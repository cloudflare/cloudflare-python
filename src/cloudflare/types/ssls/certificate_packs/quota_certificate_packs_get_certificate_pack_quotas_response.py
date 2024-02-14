# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...._models import BaseModel
from ....types import shared

__all__ = ["QuotaCertificatePacksGetCertificatePackQuotasResponse", "Advanced"]


class Advanced(BaseModel):
    allocated: Optional[int] = None
    """Quantity Allocated."""

    used: Optional[int] = None
    """Quantity Used."""


class QuotaCertificatePacksGetCertificatePackQuotasResponse(BaseModel):
    advanced: Optional[Advanced] = None
