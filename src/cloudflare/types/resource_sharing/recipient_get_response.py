# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RecipientGetResponse", "Resource"]


class Resource(BaseModel):
    error: str
    """Share Recipient error message."""

    resource_id: str
    """Share Resource identifier."""

    resource_version: int
    """Resource Version."""


class RecipientGetResponse(BaseModel):
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

    resources: Optional[List[Resource]] = None
