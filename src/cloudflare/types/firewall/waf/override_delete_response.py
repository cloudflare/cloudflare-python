# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["OverrideDeleteResponse"]


class OverrideDeleteResponse(BaseModel):
    id: Optional[str] = None
    """The unique identifier of the WAF override."""
