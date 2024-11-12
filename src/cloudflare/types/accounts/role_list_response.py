# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from ..shared.permission_grant import PermissionGrant

__all__ = ["RoleListResponse", "Permissions"]


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


class RoleListResponse(BaseModel):
    id: str
    """Role identifier tag."""

    description: str
    """Description of role's permissions."""

    name: str
    """Role name."""

    permissions: Permissions
