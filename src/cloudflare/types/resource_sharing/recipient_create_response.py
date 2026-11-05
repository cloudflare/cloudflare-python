# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RecipientCreateResponse", "Resource"]


class Resource(BaseModel):
    error: str
    """Error from the most recent attempt to apply the resource to the recipient.

    Empty string when no error has been recorded.
    """

    resource_id: str
    """Identifier assigned by the service that owns the shared resource."""

    resource_version: Optional[int] = None
    """Resource version applied to the recipient, if reconciliation has occurred."""

    terminal: Optional[bool] = None
    """Whether the error is terminal or will be continually retried."""


class RecipientCreateResponse(BaseModel):
    """A recipient of a share.

    The `association_status` field tracks the
    lifecycle of the shared resources in the recipient account. All
    recipients are returned by the list endpoint regardless of status;
    filter client-side if only active recipients are needed.
    """

    id: str
    """Share Recipient identifier tag."""

    account_id: str
    """Account identifier."""

    association_status: Literal["associating", "associated", "disassociating", "disassociated"]
    """The current state of the recipient relative to the share.

    The `desired_association_status` (not exposed in the response) tracks the target
    state set by the API; the background reconciliation workflow drives
    `current_association_status` toward it.

    - `associating` — The recipient was recently added; the workflow is pushing
      shared resources into the recipient account.
    - `associated` — Shared resources have been successfully applied to the
      recipient account.
    - `disassociating` — The recipient was removed (via DELETE or PUT replacement);
      the workflow is removing shared resources from the recipient account.
    - `disassociated` — Shared resources have been removed from the recipient
      account. The recipient record remains in the database.
    """

    created: datetime
    """When the object was created."""

    modified: datetime
    """When the object was last modified."""

    resources: Optional[List[Resource]] = None
