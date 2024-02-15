# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["ProxyReadTimeoutUpdateParams", "Value"]


class ProxyReadTimeoutUpdateParams(TypedDict, total=False):
    value: Required[Value]
    """Maximum time between two read operations from origin."""


class Value(TypedDict, total=False):
    id: Required[Literal["proxy_read_timeout"]]
    """ID of the zone setting."""

    value: Required[float]
    """Current value of the zone setting."""
