# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["NAPTRRecord", "Data"]


class Data(BaseModel):
    flags: Optional[str] = None
    """Flags."""

    order: Optional[float] = None
    """Order."""

    preference: Optional[float] = None
    """Preference."""

    regex: Optional[str] = None
    """Regex."""

    replacement: Optional[str] = None
    """Replacement."""

    service: Optional[str] = None
    """Service."""


class NAPTRRecord(BaseModel):
    content: Optional[str] = None
    """Formatted NAPTR content. See 'data' to set NAPTR properties."""

    data: Optional[Data] = None
    """Components of a NAPTR record."""

    type: Optional[Literal["NAPTR"]] = None
    """Record type."""
