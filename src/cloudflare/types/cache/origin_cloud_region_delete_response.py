# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["OriginCloudRegionDeleteResponse"]


class OriginCloudRegionDeleteResponse(BaseModel):
    """Response result for a delete operation. Identifies the deleted mapping."""

    origin_ip: str
    """The origin IP address whose mapping was deleted."""
