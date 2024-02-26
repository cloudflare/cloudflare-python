# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PrefixEditParams"]


class PrefixEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    description: Required[str]
    """Description of the prefix."""
