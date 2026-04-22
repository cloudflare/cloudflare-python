# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["OriginCloudRegionBulkEditResponse", "Value", "ValueFailed", "ValueSucceeded"]


class ValueFailed(BaseModel):
    """Result for a single item in a batch operation."""

    origin_ip: str = FieldInfo(alias="origin-ip")
    """The origin IP address for this item."""

    error: Optional[str] = None
    """Error message explaining why the item failed. Present only on failed items."""

    region: Optional[str] = None
    """Cloud vendor region identifier.

    Present on succeeded items for patch operations.
    """

    vendor: Optional[str] = None
    """Cloud vendor identifier. Present on succeeded items for patch operations."""


class ValueSucceeded(BaseModel):
    """Result for a single item in a batch operation."""

    origin_ip: str = FieldInfo(alias="origin-ip")
    """The origin IP address for this item."""

    error: Optional[str] = None
    """Error message explaining why the item failed. Present only on failed items."""

    region: Optional[str] = None
    """Cloud vendor region identifier.

    Present on succeeded items for patch operations.
    """

    vendor: Optional[str] = None
    """Cloud vendor identifier. Present on succeeded items for patch operations."""


class Value(BaseModel):
    failed: List[ValueFailed]
    """Items that could not be applied, with error details."""

    succeeded: List[ValueSucceeded]
    """Items that were successfully applied."""


class OriginCloudRegionBulkEditResponse(BaseModel):
    """Response result for a batch origin cloud region operation."""

    id: Literal["origin_public_cloud_region"]

    editable: bool
    """Whether the setting can be modified by the current user."""

    value: Value

    modified_on: Optional[datetime] = None
    """Time the mapping set was last modified.

    Null when no items were successfully applied.
    """
