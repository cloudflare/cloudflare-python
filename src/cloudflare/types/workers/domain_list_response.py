# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["DomainListResponse"]


class DomainListResponse(BaseModel):
    id: str
    """Immutable ID of the domain."""

    cert_id: str
    """ID of the TLS certificate issued for the domain."""

    enabled: bool
    """Whether the configured hostname is routable for the domain.

    If disabled, then requests to the configured hostname will not be routed to the
    configured Worker. If disabled, then preview routing must be enabled, and only
    subdomains of the configured hostname will be routable.
    """

    environment: str
    """Worker environment associated with the domain."""

    hostname: str
    """Hostname of the domain.

    Can be either the zone apex or a subdomain of the zone. Requests to this
    hostname will be routed to the configured Worker.
    """

    previews_enabled: bool
    """Whether previews are routable for the domain.

    If enabled, previews will be routable as subdomains of the configured hostname.
    For example, if the configured hostname is `app.example.com`, then requests to
    `my-feature.app.example.com` will be routed to the preview with slug
    `my-feature`, if such a preview exists. If preview routing is disabled, then
    hostname routing must be enabled.
    """

    service: str
    """Name of the Worker associated with the domain.

    Requests to the configured hostname will be routed to this Worker.
    """

    zone_id: str
    """ID of the zone containing the domain hostname."""

    zone_name: str
    """Name of the zone containing the domain hostname."""
