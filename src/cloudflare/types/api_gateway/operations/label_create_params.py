# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["LabelCreateParams"]


class LabelCreateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    managed: SequenceNotStr[str]
    """List of managed label names."""

    user: SequenceNotStr[str]
    """List of user label names."""
