# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["AssetUpdateResponse"]


class AssetUpdateResponse(BaseModel):
    description: Optional[str] = None
    """A short description of the custom asset."""

    last_updated: Optional[datetime] = None

    name: Optional[str] = None
    """The unique name of the custom asset.

    Can only contain letters (A-Z, a-z), numbers (0-9), and underscores (\\__).
    """

    size_bytes: Optional[int] = None
    """The size of the asset content in bytes."""

    url: Optional[str] = None
    """The URL where the asset content is fetched from."""
