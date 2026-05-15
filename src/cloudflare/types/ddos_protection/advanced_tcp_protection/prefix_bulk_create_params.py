# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["PrefixBulkCreateParams", "Body"]


class PrefixBulkCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    body: Required[Iterable[Body]]


class Body(TypedDict, total=False):
    comment: Required[str]
    """A comment describing the prefix."""

    excluded: Required[bool]
    """Whether to exclude the prefix from protection."""

    prefix: Required[str]
    """The prefix to add in CIDR format."""
