# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["TunnelArgoTunnelCreateAnArgoTunnelParams"]


class TunnelArgoTunnelCreateAnArgoTunnelParams(TypedDict, total=False):
    name: Required[str]
    """A user-friendly name for the tunnel."""

    tunnel_secret: Required[object]
    """Sets the password required to run the tunnel.

    Must be at least 32 bytes and encoded as a base64 string.
    """
