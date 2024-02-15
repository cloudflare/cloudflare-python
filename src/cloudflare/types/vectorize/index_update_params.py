# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["IndexUpdateParams"]


class IndexUpdateParams(TypedDict, total=False):
    account_identifier: Required[str]
    """Identifier"""

    description: Required[str]
    """Specifies the description of the index."""
