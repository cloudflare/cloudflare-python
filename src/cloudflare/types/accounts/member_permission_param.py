# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .permission_grant_param import PermissionGrantParam

__all__ = ["MemberPermissionParam"]


class MemberPermissionParam(TypedDict, total=False):
    analytics: PermissionGrantParam

    billing: PermissionGrantParam

    cache_purge: PermissionGrantParam

    dns: PermissionGrantParam

    dns_records: PermissionGrantParam

    lb: PermissionGrantParam

    logs: PermissionGrantParam

    organization: PermissionGrantParam

    ssl: PermissionGrantParam

    waf: PermissionGrantParam

    zone_settings: PermissionGrantParam

    zones: PermissionGrantParam
