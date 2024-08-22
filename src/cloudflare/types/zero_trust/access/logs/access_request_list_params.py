# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal, Annotated

from typing import Union

from datetime import datetime

from ....._utils import PropertyInfo

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ....._types import FileTypes
from ....._utils import PropertyInfo

__all__ = ["AccessRequestListParams"]

class AccessRequestListParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    direction: Literal["desc", "asc"]
    """The chronological sorting order for the logs."""

    limit: int
    """The maximum number of log entries to retrieve."""

    since: Annotated[Union[str, datetime], PropertyInfo(format = "iso8601")]
    """The earliest event timestamp to query."""

    until: Annotated[Union[str, datetime], PropertyInfo(format = "iso8601")]
    """The latest event timestamp to query."""