# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Annotated

from typing import Union

from datetime import datetime

from ..._utils import PropertyInfo

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["HistoryListParams"]

class HistoryListParams(TypedDict, total=False):
    account_id: Required[str]
    """The account id"""

    before: Annotated[Union[str, datetime], PropertyInfo(format = "iso8601")]
    """Limit the returned results to history records older than the specified date.

    This must be a timestamp that conforms to RFC3339.
    """

    page: float
    """Page number of paginated results."""

    per_page: float
    """Number of items per page."""

    since: Annotated[Union[str, datetime], PropertyInfo(format = "iso8601")]
    """Limit the returned results to history records newer than the specified date.

    This must be a timestamp that conforms to RFC3339.
    """