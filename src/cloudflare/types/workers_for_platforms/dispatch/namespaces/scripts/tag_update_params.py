# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ......_types import FileTypes
from ......_utils import PropertyInfo

__all__ = ["TagUpdateParams"]

class TagUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    dispatch_namespace: Required[str]
    """Name of the Workers for Platforms dispatch namespace."""

    body: Required[List[str]]
    """Tags to help you manage your Workers"""