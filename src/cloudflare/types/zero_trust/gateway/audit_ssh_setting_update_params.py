# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AuditSSHSettingUpdateParams"]


class AuditSSHSettingUpdateParams(TypedDict, total=False):
    account_id: Required[object]

    public_key: Required[str]
    """SSH encryption public key"""

    seed_id: str
    """Seed ID"""
