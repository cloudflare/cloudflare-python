# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["OrganizationRevokeUsersParams"]


class OrganizationRevokeUsersParams(TypedDict, total=False):
    email: Required[str]
    """The email of the user to revoke."""

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    query_devices: Annotated[bool, PropertyInfo(alias="devices")]
    """When set to `true`, all devices associated with the user will be revoked."""

    body_devices: Annotated[bool, PropertyInfo(alias="devices")]
    """When set to `true`, all devices associated with the user will be revoked."""

    user_uid: str
    """The uuid of the user to revoke."""

    warp_session_reauth: bool
    """
    When set to `true`, the user will be required to re-authenticate to WARP for all
    Gateway policies that enforce a WARP client session duration. When `false`, the
    user’s WARP session will remain active
    """
