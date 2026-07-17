# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["TokenCreateParams"]


class TokenCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account identifier."""

    operations: Required[List[Literal["publish", "subscribe"]]]
    """Non-empty subset of the V1 roles the token is allowed to perform.

    Signed into the token.
    """

    expires: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Optional expiry (RFC 3339).

    Defaults to 1 year from creation; rejected if more than 1 year in the future.
    """

    label: str
    """Optional, customer-set label."""
