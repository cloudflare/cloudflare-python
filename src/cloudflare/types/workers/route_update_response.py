# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ..._models import BaseModel

__all__ = ["RouteUpdateResponse"]


class RouteUpdateResponse(BaseModel):
    id: str
    """Identifier."""

    pattern: str
    """Pattern to match incoming requests against.

    [Learn more](https://developers.cloudflare.com/workers/configuration/routing/routes/#matching-behavior).
    """

    script: str
    """Name of the script to run if the route matches."""
