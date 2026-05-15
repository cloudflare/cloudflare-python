# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PrefixCreateParams"]


class PrefixCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    comment: Required[str]
    """A comment describing the prefix."""

    excluded: Required[bool]
    """Whether to exclude the prefix from protection."""

    prefix: Required[str]
    """The prefix to add in CIDR format."""
