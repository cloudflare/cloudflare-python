# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["LabelUpdateParams"]


class LabelUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    managed: SequenceNotStr[str]
    """List of managed label names.

    Omitting this property or passing an empty array will result in all managed
    labels being removed from the operation
    """

    user: SequenceNotStr[str]
    """List of user label names.

    Omitting this property or passing an empty array will result in all user labels
    being removed from the operation
    """
