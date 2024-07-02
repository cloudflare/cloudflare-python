# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["CustomPageUpdateParams"]


class CustomPageUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    custom_html: Required[str]
    """Custom page HTML."""

    name: Required[str]
    """Custom page name."""

    type: Required[Literal["identity_denied", "forbidden"]]
    """Custom page type."""

    app_count: int
    """Number of apps the custom page is assigned to."""

    created_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    uid: str
    """UUID"""

    updated_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
