# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ZoneEditParams"]


class ZoneEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    paused: bool
    """Indicates whether the zone is only using Cloudflare DNS services.

    A true value means the zone will not receive security or performance benefits.
    """

    type: Literal["full", "partial", "secondary", "internal"]
    """A full zone implies that DNS is hosted with Cloudflare.

    A partial zone is typically a partner-hosted zone or a CNAME setup. This
    parameter is only available to Enterprise customers or if it has been explicitly
    enabled on a zone.
    """

    vanity_name_servers: List[str]
    """An array of domains used for custom name servers.

    This is only available for Business and Enterprise plans.
    """
