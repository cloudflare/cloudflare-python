# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AllowlistCreateParams"]


class AllowlistCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    comment: Required[str]
    """An comment describing the allowlist prefix."""

    enabled: Required[bool]
    """Whether to enable the allowlist prefix into effect."""

    prefix: Required[str]
    """The allowlist prefix to add in CIDR format."""
