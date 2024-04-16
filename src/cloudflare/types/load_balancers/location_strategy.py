# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["LocationStrategy"]


class LocationStrategy(BaseModel):
    mode: Optional[Literal["pop", "resolver_ip"]] = None
    """
    Determines the authoritative location when ECS is not preferred, does not exist
    in the request, or its GeoIP lookup is unsuccessful.

    - `"pop"`: Use the Cloudflare PoP location.
    - `"resolver_ip"`: Use the DNS resolver GeoIP location. If the GeoIP lookup is
      unsuccessful, use the Cloudflare PoP location.
    """

    prefer_ecs: Optional[Literal["always", "never", "proximity", "geo"]] = None
    """
    Whether the EDNS Client Subnet (ECS) GeoIP should be preferred as the
    authoritative location.

    - `"always"`: Always prefer ECS.
    - `"never"`: Never prefer ECS.
    - `"proximity"`: Prefer ECS only when `steering_policy="proximity"`.
    - `"geo"`: Prefer ECS only when `steering_policy="geo"`.
    """
