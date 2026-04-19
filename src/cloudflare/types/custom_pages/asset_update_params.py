# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AssetUpdateParams"]


class AssetUpdateParams(TypedDict, total=False):
    description: Required[str]
    """A short description of the custom asset."""

    url: Required[str]
    """The URL where the asset content is fetched from."""

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""
