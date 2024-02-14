# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Literal

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["PageruleListParams"]


class PageruleListParams(TypedDict, total=False):
    direction: Literal["asc", "desc"]
    """The direction used to sort returned Page Rules."""

    match: Literal["any", "all"]
    """When set to `all`, all the search requirements must match.

    When set to `any`, only one of the search requirements has to match.
    """

    order: Literal["status", "priority"]
    """The field used to sort returned Page Rules."""

    status: Literal["active", "disabled"]
    """The status of the Page Rule."""
