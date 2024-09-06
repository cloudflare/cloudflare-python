# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, List

from ..shared.permission_grant import PermissionGrant

from ..accounts.account import Account

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["Membership", "Permissions"]


class Permissions(BaseModel):
    analytics: Optional[PermissionGrant] = None

    billing: Optional[PermissionGrant] = None

    cache_purge: Optional[PermissionGrant] = None

    dns: Optional[PermissionGrant] = None

    dns_records: Optional[PermissionGrant] = None

    lb: Optional[PermissionGrant] = None

    logs: Optional[PermissionGrant] = None

    organization: Optional[PermissionGrant] = None

    ssl: Optional[PermissionGrant] = None

    waf: Optional[PermissionGrant] = None

    zone_settings: Optional[PermissionGrant] = None

    zones: Optional[PermissionGrant] = None


class Membership(BaseModel):
    id: Optional[str] = None
    """Membership identifier tag."""

    account: Optional[Account] = None

    api_access_enabled: Optional[bool] = None
    """Enterprise only.

    Indicates whether or not API access is enabled specifically for this user on a
    given account.
    """

    permissions: Optional[Permissions] = None
    """All access permissions for the user at the account."""

    roles: Optional[List[str]] = None
    """List of role names for the user at the account."""

    status: Optional[Literal["accepted", "pending", "rejected"]] = None
    """Status of this membership."""
