# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ....._models import BaseModel

__all__ = ["AssetSchemaListResponse", "AssetClass"]


class AssetClass(BaseModel):
    asset_class: str
    """Asset class identifier (PascalCase), e.g. AnthropicUser."""


class AssetSchemaListResponse(BaseModel):
    asset_classes: List[AssetClass]
    """Asset classes belonging to this vendor, sorted by asset_class."""

    vendor: str
    """Canonical vendor enum value, e.g. GOOGLE_WORKSPACE."""
