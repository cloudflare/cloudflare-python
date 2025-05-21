# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["SecretCreateResponse"]


class SecretCreateResponse(BaseModel):
    id: str
    """Secret identifier tag."""

    created: datetime
    """Whenthe secret was created."""

    modified: datetime
    """When the secret was modified."""

    name: str
    """The name of the secret"""

    status: Literal["pending", "active", "deleted"]

    store_id: str
    """Store Identifier"""

    comment: Optional[str] = None
    """Freeform text describing the secret"""
