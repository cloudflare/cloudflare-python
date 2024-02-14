# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import Iterable

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["IncomingSecondaryDNSSecondaryZoneUpdateSecondaryZoneConfigurationParams"]


class IncomingSecondaryDNSSecondaryZoneUpdateSecondaryZoneConfigurationParams(TypedDict, total=False):
    auto_refresh_seconds: Required[float]
    """
    How often should a secondary zone auto refresh regardless of DNS NOTIFY. Not
    applicable for primary zones.
    """

    name: Required[str]
    """Zone name."""

    peers: Required[Iterable[object]]
    """A list of peer tags."""
