# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["ScopeParam"]


class ScopeParam(TypedDict, total=False):
    """Used only for ECMP routes."""

    colo_names: SequenceNotStr[str]
    """List of colo names for the ECMP scope."""

    colo_regions: SequenceNotStr[str]
    """List of colo regions for the ECMP scope."""
