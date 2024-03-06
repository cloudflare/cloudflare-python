# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["CaptionGetResponse", "CaptionGetResponseItem"]


class CaptionGetResponseItem(BaseModel):
    label: Optional[str] = None
    """The language label displayed in the native language to users."""

    language: Optional[str] = None
    """The language tag in BCP 47 format."""


CaptionGetResponse = List[CaptionGetResponseItem]
