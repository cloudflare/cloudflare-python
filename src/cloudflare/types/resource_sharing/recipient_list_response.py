# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RecipientListResponse"]


class RecipientListResponse(BaseModel):
    id: str
    """Share Recipient identifier tag."""

    account_id: str
    """Account identifier."""

    association_status: Literal["associating", "associated", "disassociating", "disassociated"]
    """Share Recipient association status."""

    created: datetime
    """When the share was created."""

    modified: datetime
    """When the share was modified."""

    status_message: str
    """Share Recipient status message."""
