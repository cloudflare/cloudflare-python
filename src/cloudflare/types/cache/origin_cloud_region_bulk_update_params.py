# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["OriginCloudRegionBulkUpdateParams", "Body"]


class OriginCloudRegionBulkUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    body: Required[Iterable[Body]]


class Body(TypedDict, total=False):
    """Request body for creating or replacing an origin cloud region mapping."""

    origin_ip: Required[str]
    """Origin IP address (IPv4 or IPv6).

    For the single PUT endpoint (`PUT /origin/cloud_regions/{origin_ip}`), this
    field must match the path parameter or the request will be rejected with a 400
    error. For the batch PUT endpoint, this field identifies which mapping to
    upsert.
    """

    region: Required[str]
    """Cloud vendor region identifier.

    Must be a valid region for the specified vendor as returned by the
    supported_regions endpoint.
    """

    vendor: Required[Literal["aws", "azure", "gcp", "oci"]]
    """Cloud vendor hosting the origin. Must be one of the supported vendors."""
