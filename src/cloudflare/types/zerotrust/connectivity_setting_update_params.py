# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["ConnectivitySettingUpdateParams"]


class ConnectivitySettingUpdateParams(TypedDict, total=False):
    icmp_proxy_enabled: bool
    """A flag to enable the ICMP proxy for the account network."""

    offramp_warp_enabled: bool
    """A flag to enable WARP to WARP traffic."""
