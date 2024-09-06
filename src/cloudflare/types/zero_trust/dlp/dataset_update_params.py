# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import Optional

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo

__all__ = ["DatasetUpdateParams"]


class DatasetUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    description: Optional[str]
    """The description of the dataset"""

    name: Optional[str]
    """The name of the dataset, must be unique"""
