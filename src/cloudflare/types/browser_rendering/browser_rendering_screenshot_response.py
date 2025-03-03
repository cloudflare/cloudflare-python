# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["BrowserRenderingScreenshotResponse", "Error"]


class Error(BaseModel):
    code: float
    """Error code"""

    message: str
    """Error Message"""


class BrowserRenderingScreenshotResponse(BaseModel):
    status: bool
    """Response status"""

    errors: Optional[List[Error]] = None
