# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["PreviewCreateResponse"]


class PreviewCreateResponse(BaseModel):
    screenshot: str

    error: Optional[str] = None
