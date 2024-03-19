# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["VideoStorageUsageResponse"]


class VideoStorageUsageResponse(BaseModel):
    creator: Optional[str] = None
    """A user-defined identifier for the media creator."""

    total_storage_minutes: Optional[int] = FieldInfo(alias="totalStorageMinutes", default=None)
    """The total minutes of video content stored in the account."""

    total_storage_minutes_limit: Optional[int] = FieldInfo(alias="totalStorageMinutesLimit", default=None)
    """The storage capacity alloted for the account."""

    video_count: Optional[int] = FieldInfo(alias="videoCount", default=None)
    """The total count of videos associated with the account."""
