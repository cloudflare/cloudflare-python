# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["LabelBulkUpdateParams", "Managed", "Selector", "SelectorInclude", "User"]


class LabelBulkUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    managed: Required[Managed]
    """Managed labels to replace for all affected operations"""

    selector: Required[Selector]
    """Operation IDs selector"""

    user: Required[User]
    """User labels to replace for all affected operations"""


class Managed(TypedDict, total=False):
    """Managed labels to replace for all affected operations"""

    labels: Required[SequenceNotStr[str]]
    """List of managed label names.

    Providing an empty array will result in all managed labels being removed from
    all affected operations
    """


class SelectorInclude(TypedDict, total=False):
    operation_ids: Required[SequenceNotStr[str]]


class Selector(TypedDict, total=False):
    """Operation IDs selector"""

    include: Required[SelectorInclude]


class User(TypedDict, total=False):
    """User labels to replace for all affected operations"""

    labels: Required[SequenceNotStr[str]]
    """List of user label names.

    Providing an empty array will result in all user labels being removed from all
    affected operations
    """
