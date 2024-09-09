# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .header_param import HeaderParam

__all__ = ["OriginParam"]


class OriginParam(TypedDict, total=False):
    address: str
    """
    The IP address (IPv4 or IPv6) of the origin, or its publicly addressable
    hostname. Hostnames entered here should resolve directly to the origin, and not
    be a hostname proxied by Cloudflare. To set an internal/reserved address,
    virtual_network_id must also be set.
    """

    enabled: bool
    """Whether to enable (the default) this origin within the pool.

    Disabled origins will not receive traffic and are excluded from health checks.
    The origin will only be disabled for the current pool.
    """

    header: HeaderParam
    """The request header is used to pass additional information with an HTTP request.

    Currently supported header is 'Host'.
    """

    name: str
    """A human-identifiable name for the origin."""

    virtual_network_id: str
    """The virtual network subnet ID the origin belongs in.

    Virtual network must also belong to the account.
    """

    weight: float
    """The weight of this origin relative to other origins in the pool.

    Based on the configured weight the total traffic is distributed among origins
    within the pool.

    - `origin_steering.policy="least_outstanding_requests"`: Use weight to scale the
      origin's outstanding requests.
    - `origin_steering.policy="least_connections"`: Use weight to scale the origin's
      open connections.
    """
