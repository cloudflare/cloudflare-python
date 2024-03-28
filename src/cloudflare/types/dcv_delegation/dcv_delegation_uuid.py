# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["DCVDelegationUUID"]


class DCVDelegationUUID(BaseModel):
    uuid: Optional[str] = None
    """The DCV Delegation unique identifier."""
