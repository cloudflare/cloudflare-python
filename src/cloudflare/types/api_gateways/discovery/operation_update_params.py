# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import Dict

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo
from ....types import shared_params

__all__ = ["OperationUpdateParams", "Body"]


class OperationUpdateParams(TypedDict, total=False):
    body: Required[Dict[str, Body]]


class Body(TypedDict, total=False):
    state: Literal["review", "ignored"]
    """Mark state of operation in API Discovery

    - `review` - Mark operation as for review
    - `ignored` - Mark operation as ignored
    """
