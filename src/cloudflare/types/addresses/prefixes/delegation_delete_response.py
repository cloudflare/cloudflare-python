# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ...._models import BaseModel

__all__ = ["DelegationDeleteResponse"]


class DelegationDeleteResponse(BaseModel):
    id: Optional[str] = None
    """Delegation identifier tag."""
