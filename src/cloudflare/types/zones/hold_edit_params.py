# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["HoldEditParams"]


class HoldEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    hold_after: str
    """
    If `hold_after` is provided and future-dated, the hold will be temporarily
    disabled, then automatically re-enabled by the system at the time specified in
    this RFC3339-formatted timestamp. A past-dated `hold_after` value will have no
    effect on an existing, enabled hold. Providing an empty string will set its
    value to the current time.
    """

    include_subdomains: bool
    """
    If `true`, the zone hold will extend to block any subdomain of the given zone,
    as well as SSL4SaaS Custom Hostnames. For example, a zone hold on a zone with
    the hostname 'example.com' and include_subdomains=true will block 'example.com',
    'staging.example.com', 'api.staging.example.com', etc.
    """
