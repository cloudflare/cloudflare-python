# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["UserUpdateParams"]


class UserUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    description: str
    """The description of the label"""

    metadata: object
    """Metadata for the label"""
