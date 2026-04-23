# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["OriginCloudRegionCreateParams"]


class OriginCloudRegionCreateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    ip: Required[str]
    """Origin IP address (IPv4 or IPv6).

    Normalized to canonical form before storage (RFC 5952 for IPv6).
    """

    region: Required[str]
    """Cloud vendor region identifier.

    Must be a valid region for the specified vendor as returned by the
    supported_regions endpoint.
    """

    vendor: Required[Literal["aws", "azure", "gcp", "oci"]]
    """Cloud vendor hosting the origin. Must be one of the supported vendors."""
