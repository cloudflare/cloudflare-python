# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["UserBulkCreateParams", "Body"]


class UserBulkCreateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    body: Required[Iterable[Body]]


class Body(TypedDict, total=False):
    name: Required[str]
    """The name of the label"""

    description: str
    """The description of the label"""

    metadata: object
    """Metadata for the label"""
