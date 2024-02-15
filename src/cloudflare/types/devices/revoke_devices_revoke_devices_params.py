# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["RevokeDevicesRevokeDevicesParams"]


class RevokeDevicesRevokeDevicesParams(TypedDict, total=False):
    body: Required[List[str]]
    """A list of device ids to revoke."""
