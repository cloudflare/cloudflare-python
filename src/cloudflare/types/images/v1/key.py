# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["Key"]


class Key(BaseModel):
    name: Optional[str] = None
    """Key name."""

    value: Optional[str] = None
    """Key value."""
