# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ResourceSharingGetResponse", "Resource"]


class Resource(BaseModel):
    id: str
    """Share Resource identifier."""

    created: datetime
    """When the share was created."""

    meta: object
    """Resource Metadata."""

    modified: datetime
    """When the share was modified."""

    resource_account_id: str
    """Account identifier."""

    resource_id: str
    """Share Resource identifier."""

    resource_type: Literal[
        "custom-ruleset",
        "widget",
        "gateway-policy",
        "gateway-destination-ip",
        "gateway-block-page-settings",
        "gateway-extended-email-matching",
    ]
    """Resource Type."""

    resource_version: int
    """Resource Version."""

    status: Literal["active", "deleting", "deleted"]
    """Resource Status."""


class ResourceSharingGetResponse(BaseModel):
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

    associated_recipient_count: Optional[int] = None
    """The number of recipients in the 'associated' state.

    This field is only included when requested via the 'include_recipient_counts'
    parameter.
    """

    associating_recipient_count: Optional[int] = None
    """The number of recipients in the 'associating' state.

    This field is only included when requested via the 'include_recipient_counts'
    parameter.
    """

    disassociated_recipient_count: Optional[int] = None
    """The number of recipients in the 'disassociated' state.

    This field is only included when requested via the 'include_recipient_counts'
    parameter.
    """

    disassociating_recipient_count: Optional[int] = None
    """The number of recipients in the 'disassociating' state.

    This field is only included when requested via the 'include_recipient_counts'
    parameter.
    """

    kind: Optional[Literal["sent", "received"]] = None

    resources: Optional[List[Resource]] = None
    """A list of resources that are part of the share.

    This field is only included when requested via the 'include_resources'
    parameter.
    """
