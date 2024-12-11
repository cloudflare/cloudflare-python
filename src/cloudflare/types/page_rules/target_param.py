# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TargetParam", "Constraint"]


class Constraint(TypedDict, total=False):
    operator: Required[Literal["matches", "contains", "equals", "not_equal", "not_contain"]]
    """
    The matches operator can use asterisks and pipes as wildcard and 'or' operators.
    """

    value: Required[str]
    """The URL pattern to match against the current request.

    The pattern may contain up to four asterisks ('\\**') as placeholders.
    """


class TargetParam(TypedDict, total=False):
    constraint: Constraint
    """String constraint."""

    target: Literal["url"]
    """A target based on the URL of the request."""
