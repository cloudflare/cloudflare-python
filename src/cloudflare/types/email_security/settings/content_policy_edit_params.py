# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ContentPolicyEditParams"]


class ContentPolicyEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    enabled: bool
    """Whether the policy is active."""

    name: str
    """Human-readable name of the policy."""

    notes: Optional[str]
    """Optional note describing the purpose of the policy."""

    pattern: str
    """Regular expression the policy matches against."""

    targets: List[Literal["SUBJECT", "BODY"]]
    """Parts of the email the pattern is matched against."""
