# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["IncomingUpdateParams"]


class IncomingUpdateParams(TypedDict, total=False):
    zone_id: Required[str]

    auto_refresh_seconds: Required[float]
    """
    How often should a secondary zone auto refresh regardless of DNS NOTIFY. Not
    applicable for primary zones.
    """

    name: Required[str]
    """Zone name."""

    peers: Required[List[str]]
    """A list of peer tags."""
