# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import Iterable

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo
from ....types import shared_params

__all__ = ["IncludeDevicesSetSplitTunnelIncludeListForADeviceSettingsPolicyParams", "Body"]


class IncludeDevicesSetSplitTunnelIncludeListForADeviceSettingsPolicyParams(TypedDict, total=False):
    identifier: Required[object]

    body: Required[Iterable[Body]]


class Body(TypedDict, total=False):
    address: Required[str]
    """The address in CIDR format to include in the tunnel.

    If address is present, host must not be present.
    """

    description: Required[str]
    """A description of the split tunnel item, displayed in the client UI."""

    host: str
    """The domain name to include in the tunnel.

    If host is present, address must not be present.
    """
