# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["DatabaseQueryParams"]


class DatabaseQueryParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier tag."""

    sql: Required[str]
    """Your SQL query.

    Supports multiple statements, joined by semicolons, which will be executed as a
    batch.
    """

    params: List[str]
