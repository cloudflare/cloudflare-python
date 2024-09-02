# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Iterable

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["BrandProtectionURLInfoParams"]


class BrandProtectionURLInfoParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    url: List[str]
    """Submission URL(s) to filter submission results by."""

    url_id: Iterable[int]
    """Submission ID(s) to filter submission results by."""
