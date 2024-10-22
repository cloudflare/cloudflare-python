# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CERTRecord", "Data"]


class Data(BaseModel):
    algorithm: Optional[float] = None
    """Algorithm."""

    certificate: Optional[str] = None
    """Certificate."""

    key_tag: Optional[float] = None
    """Key Tag."""

    type: Optional[float] = None
    """Type."""


class CERTRecord(BaseModel):
    content: Optional[str] = None
    """Formatted CERT content. See 'data' to set CERT properties."""

    data: Optional[Data] = None
    """Components of a CERT record."""

    type: Optional[Literal["CERT"]] = None
    """Record type."""
