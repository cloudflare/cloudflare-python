# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["LocationStrategyParam"]


class LocationStrategyParam(TypedDict, total=False):
    mode: Literal["pop", "resolver_ip"]
    """
    Determines the authoritative location when ECS is not preferred, does not exist
    in the request, or its GeoIP lookup is unsuccessful.

    - `"pop"`: Use the Cloudflare PoP location.
    - `"resolver_ip"`: Use the DNS resolver GeoIP location. If the GeoIP lookup is
      unsuccessful, use the Cloudflare PoP location.
    """

    prefer_ecs: Literal["always", "never", "proximity", "geo"]
    """
    Whether the EDNS Client Subnet (ECS) GeoIP should be preferred as the
    authoritative location.

    - `"always"`: Always prefer ECS.
    - `"never"`: Never prefer ECS.
    - `"proximity"`: Prefer ECS only when `steering_policy="proximity"`.
    - `"geo"`: Prefer ECS only when `steering_policy="geo"`.
    """
