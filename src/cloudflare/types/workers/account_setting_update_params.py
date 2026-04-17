# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AccountSettingUpdateParams"]


class AccountSettingUpdateParams(TypedDict, total=False):
    account_id: str
    """Identifier."""

    default_usage_model: str

    green_compute: bool
