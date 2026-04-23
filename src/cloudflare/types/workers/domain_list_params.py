# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DomainListParams"]


class DomainListParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    environment: str
    """Worker environment associated with the domain."""

    hostname: str
    """Hostname of the domain."""

    service: str
    """Name of the Worker associated with the domain."""

    zone_id: str
    """ID of the zone containing the domain hostname."""

    zone_name: str
    """Name of the zone containing the domain hostname."""
