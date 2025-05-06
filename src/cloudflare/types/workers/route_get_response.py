# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ..._models import BaseModel

__all__ = ["RouteGetResponse"]


class RouteGetResponse(BaseModel):
    id: str
    """Identifier"""

    pattern: str

    script: str
    """Name of the script, used in URLs and route configuration."""
