# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["BlockSenderEditParams"]


class BlockSenderEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Account Identifier"""

    comments: Optional[str]

    is_regex: Optional[bool]

    pattern: Optional[str]

    pattern_type: Optional[Literal["EMAIL", "DOMAIN", "IP", "UNKNOWN"]]
