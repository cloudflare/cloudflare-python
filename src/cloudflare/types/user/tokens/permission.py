# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel
from ...accounts import PermissionGrant

__all__ = ["Permission"]


class Permission(BaseModel):
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
