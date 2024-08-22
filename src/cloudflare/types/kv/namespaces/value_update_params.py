# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ValueUpdateParams"]


class ValueUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    namespace_id: Required[str]
    """Namespace identifier tag."""

    metadata: Required[str]
    """Arbitrary JSON to be associated with a key/value pair."""

    value: Required[str]
    """A byte sequence to be stored, up to 25 MiB in length."""
