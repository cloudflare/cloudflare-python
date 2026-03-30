# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AssetCreateParams"]


class AssetCreateParams(TypedDict, total=False):
    description: Required[str]
    """A short description of the custom asset."""

    name: Required[str]
    """The unique name of the custom asset.

    Can only contain letters (A-Z, a-z), numbers (0-9), and underscores (\\__).
    """

    url: Required[str]
    """The URL where the asset content is fetched from."""

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""
