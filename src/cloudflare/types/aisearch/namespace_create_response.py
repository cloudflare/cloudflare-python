# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["NamespaceCreateResponse"]


class NamespaceCreateResponse(BaseModel):
    created_at: datetime

    name: str

    description: Optional[str] = None
    """Optional description for the namespace. Max 256 characters."""
