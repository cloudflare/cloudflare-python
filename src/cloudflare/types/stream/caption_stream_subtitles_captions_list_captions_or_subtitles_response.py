# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = [
    "CaptionStreamSubtitlesCaptionsListCaptionsOrSubtitlesResponse",
    "CaptionStreamSubtitlesCaptionsListCaptionsOrSubtitlesResponseItem",
]


class CaptionStreamSubtitlesCaptionsListCaptionsOrSubtitlesResponseItem(BaseModel):
    label: Optional[str] = None
    """The language label displayed in the native language to users."""

    language: Optional[str] = None
    """The language tag in BCP 47 format."""


CaptionStreamSubtitlesCaptionsListCaptionsOrSubtitlesResponse = List[
    CaptionStreamSubtitlesCaptionsListCaptionsOrSubtitlesResponseItem
]
