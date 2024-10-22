# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["DSRecord", "Data"]


class Data(BaseModel):
    algorithm: Optional[float] = None
    """Algorithm."""

    digest: Optional[str] = None
    """Digest."""

    digest_type: Optional[float] = None
    """Digest Type."""

    key_tag: Optional[float] = None
    """Key Tag."""


class DSRecord(BaseModel):
    content: Optional[str] = None
    """Formatted DS content. See 'data' to set DS properties."""

    data: Optional[Data] = None
    """Components of a DS record."""

    type: Optional[Literal["DS"]] = None
    """Record type."""
