# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["EmailSendingSendResponse"]


class EmailSendingSendResponse(BaseModel):
    delivered: List[str]
    """Email addresses to which the message was delivered immediately."""

    permanent_bounces: List[str]
    """Email addresses that permanently bounced."""

    queued: List[str]
    """Email addresses for which delivery was queued for later."""
