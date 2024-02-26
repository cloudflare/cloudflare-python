# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["OutgoingCreateParams"]


class OutgoingCreateParams(TypedDict, total=False):
    zone_id: Required[object]

    name: Required[str]
    """Zone name."""

    peers: Required[Iterable[object]]
    """A list of peer tags."""
