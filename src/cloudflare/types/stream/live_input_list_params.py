# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["LiveInputListParams"]


class LiveInputListParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    include_counts: bool
    """
    Includes the total number of videos associated with the submitted query
    parameters.
    """
