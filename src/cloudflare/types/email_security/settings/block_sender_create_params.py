# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["BlockSenderCreateParams"]


class BlockSenderCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account Identifier"""

    is_regex: Required[bool]

    pattern: Required[str]

    pattern_type: Required[Literal["EMAIL", "DOMAIN", "IP", "UNKNOWN"]]

    comments: Optional[str]
