# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["LabelBulkCreateParams", "Selector", "SelectorInclude", "Managed", "User"]


class LabelBulkCreateParams(TypedDict, total=False):
    zone_id: str
    """Identifier."""

    selector: Required[Selector]
    """Operation IDs selector"""

    managed: Managed

    user: User


class SelectorInclude(TypedDict, total=False):
    operation_ids: Required[SequenceNotStr[str]]


class Selector(TypedDict, total=False):
    """Operation IDs selector"""

    include: Required[SelectorInclude]


class Managed(TypedDict, total=False):
    labels: SequenceNotStr[str]
    """List of managed label names."""


class User(TypedDict, total=False):
    labels: SequenceNotStr[str]
    """List of user label names."""
