# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["IncomingCreateParams"]


class IncomingCreateParams(TypedDict, total=False):
    zone_id: Required[object]

    auto_refresh_seconds: Required[float]
    """
    How often should a secondary zone auto refresh regardless of DNS NOTIFY. Not
    applicable for primary zones.
    """

    name: Required[str]
    """Zone name."""

    peers: Required[Iterable[object]]
    """A list of peer tags."""
