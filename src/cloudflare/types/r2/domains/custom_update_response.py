# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["CustomUpdateResponse"]


class CustomUpdateResponse(BaseModel):
    domain: str
    """Domain name of the affected custom domain"""

    enabled: Optional[bool] = None
    """Whether this bucket is publicly accessible at the specified custom domain"""
