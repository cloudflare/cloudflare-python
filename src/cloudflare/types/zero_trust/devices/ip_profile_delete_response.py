# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["IPProfileDeleteResponse"]


class IPProfileDeleteResponse(BaseModel):
    id: Optional[str] = None
    """ID of the deleted Device IP profile."""
