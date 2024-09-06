# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo

__all__ = ["OperationEditParams"]


class OperationEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    state: Literal["review", "ignored"]
    """Mark state of operation in API Discovery

    - `review` - Mark operation as for review
    - `ignored` - Mark operation as ignored
    """
