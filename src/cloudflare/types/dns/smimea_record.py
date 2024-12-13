# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SMIMEARecord", "Data"]


class Data(BaseModel):
    certificate: Optional[str] = None
    """Certificate."""

    matching_type: Optional[float] = None
    """Matching Type."""

    selector: Optional[float] = None
    """Selector."""

    usage: Optional[float] = None
    """Usage."""


class SMIMEARecord(BaseModel):
    content: Optional[str] = None
    """Formatted SMIMEA content. See 'data' to set SMIMEA properties."""

    data: Optional[Data] = None
    """Components of a SMIMEA record."""

    type: Optional[Literal["SMIMEA"]] = None
    """Record type."""
