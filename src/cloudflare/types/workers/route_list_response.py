# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["RouteListResponse"]


class RouteListResponse(BaseModel):
    id: str
    """Identifier."""

    pattern: str
    """Pattern to match incoming requests against.

    [Learn more](https://developers.cloudflare.com/workers/configuration/routing/routes/#matching-behavior).
    """

    script: Optional[str] = None
    """Name of the script to run if the route matches."""
