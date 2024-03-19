# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["LiveInputListResponse", "LiveInput"]


class LiveInput(BaseModel):
    created: Optional[datetime] = None
    """The date and time the live input was created."""

    delete_recording_after_days: Optional[float] = FieldInfo(alias="deleteRecordingAfterDays", default=None)
    """
    Indicates the number of days after which the live inputs recordings will be
    deleted. When a stream completes and the recording is ready, the value is used
    to calculate a scheduled deletion date for that recording. Omit the field to
    indicate no change, or include with a `null` value to remove an existing
    scheduled deletion.
    """

    meta: Optional[object] = None
    """
    A user modifiable key-value store used to reference other systems of record for
    managing live inputs.
    """

    modified: Optional[datetime] = None
    """The date and time the live input was last modified."""

    uid: Optional[str] = None
    """A unique identifier for a live input."""


class LiveInputListResponse(BaseModel):
    live_inputs: Optional[List[LiveInput]] = FieldInfo(alias="liveInputs", default=None)

    range: Optional[int] = None
    """The total number of remaining live inputs based on cursor position."""

    total: Optional[int] = None
    """The total number of live inputs that match the provided filters."""
