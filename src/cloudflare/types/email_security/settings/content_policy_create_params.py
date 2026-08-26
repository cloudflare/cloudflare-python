# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ContentPolicyCreateParams"]


class ContentPolicyCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    enabled: Required[bool]

    name: Required[str]

    pattern: Required[str]

    targets: Required[List[Literal["SUBJECT", "BODY"]]]

    notes: Optional[str]
