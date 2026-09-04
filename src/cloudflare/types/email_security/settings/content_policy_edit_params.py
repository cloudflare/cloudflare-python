# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ContentPolicyEditParams"]


class ContentPolicyEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    enabled: bool

    name: str

    notes: Optional[str]

    pattern: str

    targets: List[Literal["SUBJECT", "BODY"]]
