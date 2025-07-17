# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel

__all__ = ["BrandProtectionURLInfoResponse"]


class BrandProtectionURLInfoResponse(BaseModel):
    code: Optional[int] = None
    """Error code"""

    errors: Optional[Dict[str, object]] = None
    """Errors"""

    message: Optional[str] = None
    """Error message"""

    status: Optional[str] = None
    """Error name"""
