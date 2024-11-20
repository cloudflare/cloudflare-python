# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["OperationBulkEditParams", "Body"]


class OperationBulkEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    body: Required[Dict[str, Body]]


class Body(TypedDict, total=False):
    state: Literal["review", "ignored"]
    """Mark state of operation in API Discovery

    - `review` - Mark operation as for review
    - `ignored` - Mark operation as ignored
    """
