# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["URIRecord", "Data"]


class Data(BaseModel):
    target: Optional[str] = None
    """The record content."""

    weight: Optional[float] = None
    """The record weight."""


class URIRecord(BaseModel):
    content: Optional[str] = None
    """Formatted URI content. See 'data' to set URI properties."""

    data: Optional[Data] = None
    """Components of a URI record."""

    priority: Optional[float] = None
    """Required for MX, SRV and URI records; unused by other record types.

    Records with lower priorities are preferred.
    """

    type: Optional[Literal["URI"]] = None
    """Record type."""
