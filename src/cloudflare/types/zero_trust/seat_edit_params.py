# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["SeatEditParams", "Body"]


class SeatEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    body: Required[Iterable[Body]]


class Body(TypedDict, total=False):
    access_seat: Required[bool]
    """True if the seat is part of Access."""

    gateway_seat: Required[bool]
    """True if the seat is part of Gateway."""

    seat_uid: Required[str]
    """The unique API identifier for the Zero Trust seat."""
