# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel

__all__ = ["PreviewCreateResponse"]


class PreviewCreateResponse(BaseModel):
    preview_url: Optional[str] = None
    """URL where the custom waiting room page can temporarily be previewed."""
