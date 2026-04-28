# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["TrustedDomainCreateParams"]


class TrustedDomainCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    is_recent: Required[bool]
    """
    Select to prevent recently registered domains from triggering a Suspicious or
    Malicious disposition.
    """

    is_regex: Required[bool]

    is_similarity: Required[bool]
    """
    Select for partner or other approved domains that have similar spelling to your
    connected domains. Prevents listed domains from triggering a Spoof disposition.
    """

    pattern: Required[str]

    comments: Optional[str]
