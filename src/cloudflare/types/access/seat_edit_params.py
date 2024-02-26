# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["SeatEditParams", "Body"]


class SeatEditParams(TypedDict, total=False):
    body: Required[Iterable[Body]]


class Body(TypedDict, total=False):
    access_seat: Required[bool]
    """True if the seat is part of Access."""

    gateway_seat: Required[bool]
    """True if the seat is part of Gateway."""
