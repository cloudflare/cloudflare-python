# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Annotated, Literal

from typing import Union

from datetime import datetime

from ...._utils import PropertyInfo

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo

__all__ = ["MessageGetParams"]


class MessageGetParams(TypedDict, total=False):
    account_identifier: Required[str]
    """Identifier"""

    page: Required[int]
    """Page number of results"""

    per_page: Required[int]
    """Number of results per page"""

    after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Retrieve messages created after this time"""

    before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Retrieve messages created before this time"""

    sort_by: str
    """Field to sort results by"""

    sort_order: Literal["asc", "desc"]
    """Sort order (asc or desc)"""
