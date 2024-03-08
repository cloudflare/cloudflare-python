# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .teams_devices_split_tunnel_include_param import TeamsDevicesSplitTunnelIncludeParam

__all__ = ["IncludeUpdateParams"]


class IncludeUpdateParams(TypedDict, total=False):
    account_id: Required[object]

    body: Required[Iterable[TeamsDevicesSplitTunnelIncludeParam]]
