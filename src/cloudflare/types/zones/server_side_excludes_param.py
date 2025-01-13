# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ServerSideExcludesParam"]


class ServerSideExcludesParam(TypedDict, total=False):
    id: Required[Literal["server_side_exclude"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""
