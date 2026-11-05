# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ResourceSharingCreateResponse", "Resource"]


class Resource(BaseModel):
    id: str
    """Share Resource identifier."""

    created: datetime
    """When the object was created."""

    meta: object
    """Resource Metadata."""

    modified: datetime
    """When the object was last modified."""

    resource_account_id: str
    """Account identifier."""

    resource_id: str
    """Identifier assigned by the service that owns the shared resource."""

    resource_type: Literal[
        "custom-ruleset",
        "gateway-policy",
        "gateway-destination-ip",
        "gateway-block-page-settings",
        "gateway-extended-email-matching",
        "idp-federation-grant",
        "trust-grant",
    ]
    """Resource Type."""

    resource_version: int
    """Resource Version."""

    status: Literal["active", "deleting", "deleted"]
    """Resource Status."""


class ResourceSharingCreateResponse(BaseModel):
    id: str
    """Share identifier tag."""

    account_id: str
    """Account identifier."""

    account_name: str
    """The display name of an account."""

    created: datetime
    """When the object was created."""

    modified: datetime
    """When the object was last modified."""

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

    tags: Optional[Dict[str, str]] = None
    """Tags associated with the share.

    Included in create and update responses when tags are supplied, and in read
    responses when the `include_tags_from` parameter is set.
    """
