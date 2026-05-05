# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["OriginCloudRegionBulkUpdateResponse", "Failed", "Succeeded"]


class Failed(BaseModel):
    """Result for a single item in a batch operation."""

    origin_ip: str
    """The origin IP address for this item."""

    error: Optional[str] = None
    """Error message explaining why the item failed. Present only on failed items."""

    region: Optional[str] = None
    """Cloud vendor region identifier.

    Present on succeeded items (the new value for upsert, the deleted value for
    delete).
    """

    vendor: Optional[str] = None
    """Cloud vendor identifier.

    Present on succeeded items (the new value for upsert, the deleted value for
    delete).
    """


class Succeeded(BaseModel):
    """Result for a single item in a batch operation."""

    origin_ip: str
    """The origin IP address for this item."""

    error: Optional[str] = None
    """Error message explaining why the item failed. Present only on failed items."""

    region: Optional[str] = None
    """Cloud vendor region identifier.

    Present on succeeded items (the new value for upsert, the deleted value for
    delete).
    """

    vendor: Optional[str] = None
    """Cloud vendor identifier.

    Present on succeeded items (the new value for upsert, the deleted value for
    delete).
    """


class OriginCloudRegionBulkUpdateResponse(BaseModel):
    """Response result for a batch origin cloud region operation."""

    failed: List[Failed]
    """Items that could not be applied, with error details."""

    succeeded: List[Succeeded]
    """Items that were successfully applied."""
