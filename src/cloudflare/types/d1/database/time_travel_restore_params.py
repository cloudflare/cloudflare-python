# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["TimeTravelRestoreParams"]


class TimeTravelRestoreParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier tag."""

    bookmark: str
    """A bookmark to restore the database to. Required if `timestamp` is not provided."""

    timestamp: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """An ISO 8601 timestamp to restore the database to.

    Required if `bookmark` is not provided.
    """
