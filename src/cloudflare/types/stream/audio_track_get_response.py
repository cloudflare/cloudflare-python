# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .audio import Audio
from ..._models import BaseModel

__all__ = ["AudioTrackGetResponse"]


class AudioTrackGetResponse(BaseModel):
    audio: Optional[List[Audio]] = None
    """Array of audio tracks for the video."""
