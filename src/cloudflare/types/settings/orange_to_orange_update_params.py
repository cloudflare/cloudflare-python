# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["OrangeToOrangeUpdateParams", "Value"]


class OrangeToOrangeUpdateParams(TypedDict, total=False):
    value: Required[Value]
    """
    Orange to Orange (O2O) allows zones on Cloudflare to CNAME to other zones also
    on Cloudflare.
    """


class Value(TypedDict, total=False):
    id: Required[Literal["orange_to_orange"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""
