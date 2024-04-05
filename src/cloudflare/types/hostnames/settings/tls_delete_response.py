# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["TLSDeleteResponse"]


class TLSDeleteResponse(BaseModel):
    created_at: Optional[datetime] = None
    """This is the time the tls setting was originally created for this hostname."""

    hostname: Optional[str] = None
    """The hostname for which the tls settings are set."""

    status: Optional[str] = None

    updated_at: Optional[datetime] = None
    """This is the time the tls setting was updated."""

    value: Optional[str] = None
