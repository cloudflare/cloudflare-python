# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ZonesPseudoIPV4Param"]


class ZonesPseudoIPV4Param(TypedDict, total=False):
    id: Required[Literal["pseudo_ipv4"]]
    """Value of the Pseudo IPv4 setting."""

    value: Required[Literal["off", "add_header", "overwrite_header"]]
    """Current value of the zone setting."""
