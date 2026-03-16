# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["DomainListResponse"]


class DomainListResponse(BaseModel):
    id: str
    """Immutable ID of the domain."""

    cert_id: str
    """ID of the TLS certificate issued for the domain."""

    environment: str
    """Worker environment associated with the domain."""

    hostname: str
    """Hostname of the domain.

    Can be either the zone apex or a subdomain of the zone. Requests to this
    hostname will be routed to the configured Worker.
    """

    service: str
    """Name of the Worker associated with the domain.

    Requests to the configured hostname will be routed to this Worker.
    """

    zone_id: str
    """ID of the zone containing the domain hostname."""

    zone_name: str
    """Name of the zone containing the domain hostname."""
