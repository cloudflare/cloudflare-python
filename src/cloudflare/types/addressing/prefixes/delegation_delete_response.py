# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["DelegationDeleteResponse"]


class DelegationDeleteResponse(BaseModel):
    id: Optional[str] = None
    """Identifier of a Delegation."""
