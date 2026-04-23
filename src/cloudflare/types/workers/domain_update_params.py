# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DomainUpdateParams"]


class DomainUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    hostname: Required[str]
    """Hostname of the domain.

    Can be either the zone apex or a subdomain of the zone. Requests to this
    hostname will be routed to the configured Worker.
    """

    service: Required[str]
    """Name of the Worker associated with the domain.

    Requests to the configured hostname will be routed to this Worker.
    """

    environment: str
    """Worker environment associated with the domain."""

    zone_id: str
    """ID of the zone containing the domain hostname."""

    zone_name: str
    """Name of the zone containing the domain hostname."""
