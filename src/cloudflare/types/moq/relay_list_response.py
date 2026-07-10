# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ..._models import BaseModel

__all__ = ["RelayListResponse"]


class RelayListResponse(BaseModel):
    """Abbreviated relay for list responses."""

    created: datetime

    modified: datetime

    name: str

    uid: str
