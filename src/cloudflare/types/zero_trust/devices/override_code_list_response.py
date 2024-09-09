# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["OverrideCodeListResponse", "DisableForTime"]


class DisableForTime(BaseModel):
    one: Optional[str] = FieldInfo(alias="1", default=None)
    """Override code that is valid for 1 hour."""

    twelve: Optional[str] = FieldInfo(alias="12", default=None)
    """Override code that is valid for 12 hour2."""

    twenty_four: Optional[str] = FieldInfo(alias="24", default=None)
    """Override code that is valid for 24 hour.2."""

    three: Optional[str] = FieldInfo(alias="3", default=None)
    """Override code that is valid for 3 hours."""

    six: Optional[str] = FieldInfo(alias="6", default=None)
    """Override code that is valid for 6 hours."""


class OverrideCodeListResponse(BaseModel):
    disable_for_time: Optional[DisableForTime] = None
