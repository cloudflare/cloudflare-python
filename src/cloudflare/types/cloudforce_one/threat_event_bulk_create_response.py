# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ThreatEventBulkCreateResponse", "Error"]


class Error(BaseModel):
    error: str
    """Error message"""

    event_index: float = FieldInfo(alias="eventIndex")
    """Index of the event that caused the error"""


class ThreatEventBulkCreateResponse(BaseModel):
    """Detailed result of bulk event creation with auto-tag management"""

    created_events_count: float = FieldInfo(alias="createdEventsCount")
    """Number of events created"""

    created_tags_count: float = FieldInfo(alias="createdTagsCount")
    """Number of new tags created in SoT"""

    error_count: float = FieldInfo(alias="errorCount")
    """Number of errors encountered"""

    queued_indicators_count: float = FieldInfo(alias="queuedIndicatorsCount")
    """Number of indicators queued for async processing"""

    skipped_events_count: float = FieldInfo(alias="skippedEventsCount")
    """Number of events skipped due to duplicate UUID (only when preserveUuid=true)"""

    create_bulk_events_request_id: Optional[str] = FieldInfo(alias="createBulkEventsRequestId", default=None)
    """Correlation ID for async indicator processing"""

    errors: Optional[List[Error]] = None
    """Array of error details"""
