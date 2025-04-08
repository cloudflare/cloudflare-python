# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ..._models import BaseModel

__all__ = ["StoreListResponse"]


class StoreListResponse(BaseModel):
    id: str
    """Store Identifier"""

    created: datetime
    """Whenthe secret was created."""

    modified: datetime
    """When the secret was modified."""

    name: str
    """The name of the store"""
