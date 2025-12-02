# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["ReleaseBulkResponse"]


class ReleaseBulkResponse(BaseModel):
    postfix_id: str
    """The identifier of the message."""

    delivered: Optional[List[str]] = None

    failed: Optional[List[str]] = None

    undelivered: Optional[List[str]] = None
