# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PatternParam"]


class PatternParam(TypedDict, total=False):
    regex: Required[str]
    """The regex pattern."""

    validation: Literal["luhn"]
    """Validation algorithm for the pattern.

    This algorithm will get run on potential matches, and if it returns false, the
    entry will not be matched.
    """
