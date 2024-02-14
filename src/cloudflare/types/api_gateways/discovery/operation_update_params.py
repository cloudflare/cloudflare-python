# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["OperationUpdateParams", "Body"]


class OperationUpdateParams(TypedDict, total=False):
    body: Required[Dict[str, Body]]


class Body(TypedDict, total=False):
    state: Literal["review", "ignored"]
    """Mark state of operation in API Discovery

    - `review` - Mark operation as for review
    - `ignored` - Mark operation as ignored
    """
