# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DomainListParams"]


class DomainListParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifer of the account."""

    environment: str
    """Worker environment associated with the zone and hostname."""

    hostname: str
    """Hostname of the Worker Domain."""

    service: str
    """Worker service associated with the zone and hostname."""

    zone_id: str
    """Identifier of the zone."""

    zone_name: str
    """Name of the zone."""
