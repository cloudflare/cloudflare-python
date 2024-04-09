# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["DNSListParams", "StartEndParams"]


class DNSListParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    ipv4: str

    page: float
    """Requested page within paginated list of results."""

    per_page: float
    """Maximum number of results requested."""

    start_end_params: StartEndParams


class StartEndParams(TypedDict, total=False):
    end: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Defaults to the current date."""

    start: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Defaults to 30 days before the end parameter value."""
