# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ThreatEventBulkCreateRelationshipsResponse", "Error"]


class Error(BaseModel):
    error: str
    """Error message"""

    event_index: float = FieldInfo(alias="eventIndex")
    """Index of the event that caused the error"""


class ThreatEventBulkCreateRelationshipsResponse(BaseModel):
    """Result of bulk relationship creation operation"""

    created_events_count: float = FieldInfo(alias="createdEventsCount")
    """Number of events created"""

    created_indicators_count: float = FieldInfo(alias="createdIndicatorsCount")
    """Number of indicators created"""

    created_relationships_count: float = FieldInfo(alias="createdRelationshipsCount")
    """Number of relationships created"""

    error_count: float = FieldInfo(alias="errorCount")
    """Number of errors encountered"""

    errors: Optional[List[Error]] = None
    """Array of error details"""
