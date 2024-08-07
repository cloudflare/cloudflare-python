# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["RetentionGetResponse"]


class RetentionGetResponse(BaseModel):
    flag: Optional[bool] = None
    """The log retention flag for Logpull API."""
