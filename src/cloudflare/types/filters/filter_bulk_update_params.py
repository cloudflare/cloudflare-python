# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["FilterBulkUpdateParams", "Body"]


class FilterBulkUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Defines an identifier."""

    body: Required[Iterable[Body]]


class Body(TypedDict, total=False):
    description: str
    """An informative summary of the filter."""

    expression: str
    """The filter expression.

    For more information, refer to
    [Expressions](https://developers.cloudflare.com/ruleset-engine/rules-language/expressions/).
    """

    paused: bool
    """When true, indicates that the filter is currently paused."""

    ref: str
    """A short reference tag. Allows you to select related filters."""
