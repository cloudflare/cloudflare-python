# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AdvertisementStatusEditParams"]


class AdvertisementStatusEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier of a Cloudflare account."""

    advertised: Required[bool]
    """Advertisement status of the prefix.

    If `true`, the BGP route for the prefix is advertised to the Internet. If
    `false`, the BGP route is withdrawn.
    """
