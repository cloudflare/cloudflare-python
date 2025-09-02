# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["OutgoingCreateParams"]


class OutgoingCreateParams(TypedDict, total=False):
    zone_id: Required[str]

    name: Required[str]
    """Zone name."""

    peers: Required[SequenceNotStr[str]]
    """A list of peer tags."""
