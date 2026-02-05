# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["LivestreamGetLivestreamAnalyticsCompleteResponse", "Data"]


class Data(BaseModel):
    count: Optional[int] = None
    """Count of total livestreams."""

    total_ingest_seconds: Optional[int] = None
    """Total time duration for which the input was given or the meeting was streamed."""

    total_viewer_seconds: Optional[int] = None
    """Total view time for which the viewers watched the stream."""


class LivestreamGetLivestreamAnalyticsCompleteResponse(BaseModel):
    data: Optional[Data] = None

    success: Optional[bool] = None
