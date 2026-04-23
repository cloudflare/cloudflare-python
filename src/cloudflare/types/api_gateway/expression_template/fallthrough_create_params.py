# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["FallthroughCreateParams"]


class FallthroughCreateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    hosts: Required[SequenceNotStr[str]]
    """List of hosts to be targeted in the expression"""
