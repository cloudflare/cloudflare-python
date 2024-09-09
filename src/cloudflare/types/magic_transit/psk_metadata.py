# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["PSKMetadata"]


class PSKMetadata(BaseModel):
    last_generated_on: Optional[datetime] = None
    """The date and time the tunnel was last modified."""
