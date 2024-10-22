# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CAARecord", "Data"]


class Data(BaseModel):
    flags: Optional[float] = None
    """Flags for the CAA record."""

    tag: Optional[str] = None
    """Name of the property controlled by this record (e.g.: issue, issuewild, iodef)."""

    value: Optional[str] = None
    """Value of the record. This field's semantics depend on the chosen tag."""


class CAARecord(BaseModel):
    content: Optional[str] = None
    """Formatted CAA content. See 'data' to set CAA properties."""

    data: Optional[Data] = None
    """Components of a CAA record."""

    type: Optional[Literal["CAA"]] = None
    """Record type."""
