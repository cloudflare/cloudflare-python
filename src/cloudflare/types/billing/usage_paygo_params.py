# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["UsagePaygoParams"]


class UsagePaygoParams(TypedDict, total=False):
    account_id: Required[str]
    """Represents a Cloudflare resource identifier tag."""

    from_: Annotated[Union[str, date], PropertyInfo(alias="from", format="iso8601")]
    """Start date for the usage query (ISO 8601)."""

    to: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """End date for the usage query (ISO 8601)."""
