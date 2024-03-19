# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["PagePreviewResponse"]


class PagePreviewResponse(BaseModel):
    preview_url: Optional[str] = None
    """URL where the custom waiting room page can temporarily be previewed."""
