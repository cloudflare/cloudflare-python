# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DeviceGetParams"]


class DeviceGetParams(TypedDict, total=False):
    account_id: Required[str]

    include: str
    """
    Comma-separated list of additional information that should be included in the
    device response. Supported values are: "last_seen_registration.policy".
    """
