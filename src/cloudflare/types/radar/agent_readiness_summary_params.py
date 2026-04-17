# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import datetime
from typing import Union
from typing_extensions import Literal, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["AgentReadinessSummaryParams"]


class AgentReadinessSummaryParams(TypedDict, total=False):
    date: Annotated[Union[str, datetime.date], PropertyInfo(format="iso8601")]
    """Filters results by the specified date."""

    domain_category: Annotated[SequenceNotStr[str], PropertyInfo(alias="domainCategory")]
    """Filters results by domain category."""

    format: Literal["JSON", "CSV"]
    """Format in which results will be returned."""

    name: SequenceNotStr[str]
    """Array of names used to label the series in the response."""
