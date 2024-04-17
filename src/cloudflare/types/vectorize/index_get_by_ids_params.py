# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["IndexGetByIDsParams"]


class IndexGetByIDsParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    ids: List[str]
    """A list of vector identifiers to retrieve from the index indicated by the path."""
