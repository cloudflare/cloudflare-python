# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SVCBRecord", "Data"]


class Data(BaseModel):
    priority: Optional[float] = None
    """priority."""

    target: Optional[str] = None
    """target."""

    value: Optional[str] = None
    """value."""


class SVCBRecord(BaseModel):
    content: Optional[str] = None
    """Formatted SVCB content. See 'data' to set SVCB properties."""

    data: Optional[Data] = None
    """Components of a SVCB record."""

    type: Optional[Literal["SVCB"]] = None
    """Record type."""
