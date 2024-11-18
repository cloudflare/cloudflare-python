# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ResourceSharingListResponse"]


class ResourceSharingListResponse(BaseModel):
    id: str
    """Share identifier tag."""

    account_id: str
    """Account identifier."""

    account_name: str
    """The display name of an account."""

    created: datetime
    """When the share was created."""

    modified: datetime
    """When the share was modified."""

    name: str
    """The name of the share."""

    organization_id: str
    """Organization identifier."""

    status: Literal["active", "deleting", "deleted"]

    target_type: Literal["account", "organization"]

    kind: Optional[Literal["sent", "received"]] = None
