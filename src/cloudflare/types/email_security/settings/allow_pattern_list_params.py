# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo

__all__ = ["AllowPatternListParams"]


class AllowPatternListParams(TypedDict, total=False):
    account_id: Required[str]
    """Account Identifier"""

    direction: Literal["asc", "desc"]
    """The sorting direction."""

    is_recipient: bool

    is_sender: bool

    is_spoof: bool

    order: Literal["pattern", "created_at"]
    """The field to sort by."""

    page: int
    """Page number of paginated results."""

    pattern_type: Literal["EMAIL", "DOMAIN", "IP", "UNKNOWN"]

    per_page: int
    """Number of results to display."""

    search: str
    """
    Allows searching in multiple properties of a record simultaneously. This
    parameter is intended for human users, not automation. Its exact behavior is
    intentionally left unspecified and is subject to change in the future.
    """

    verify_sender: bool
