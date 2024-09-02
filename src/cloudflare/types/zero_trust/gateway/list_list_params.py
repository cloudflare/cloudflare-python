# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo

__all__ = ["ListListParams"]


class ListListParams(TypedDict, total=False):
    account_id: Required[str]

    type: Literal["SERIAL", "URL", "DOMAIN", "EMAIL", "IP"]
    """The type of list."""
