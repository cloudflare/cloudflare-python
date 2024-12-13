# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TLSARecord", "Data"]


class Data(BaseModel):
    certificate: Optional[str] = None
    """certificate."""

    matching_type: Optional[float] = None
    """Matching Type."""

    selector: Optional[float] = None
    """Selector."""

    usage: Optional[float] = None
    """Usage."""


class TLSARecord(BaseModel):
    content: Optional[str] = None
    """Formatted TLSA content. See 'data' to set TLSA properties."""

    data: Optional[Data] = None
    """Components of a TLSA record."""

    type: Optional[Literal["TLSA"]] = None
    """Record type."""
