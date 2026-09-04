# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TransformerCreateParams"]


class TransformerCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    code: Required[str]
    """The SQL transformer query.

    Maximum 32 KB. The query must contain a FROM clause referencing a valid logpush
    dataset.
    """

    name: Required[str]
    """Customer-provided name for identification."""

    description: str
    """Optional customer-provided description."""
