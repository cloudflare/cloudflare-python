# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FilterCreateParams"]


class FilterCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    expression: Required[str]
    """The filter expression."""

    mode: Required[str]
    """The filter's mode. Must be one of 'enabled', 'disabled', 'monitoring'."""
