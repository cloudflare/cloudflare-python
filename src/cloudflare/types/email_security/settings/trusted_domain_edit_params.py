# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["TrustedDomainEditParams"]


class TrustedDomainEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Account Identifier"""

    comments: Optional[str]

    is_recent: Optional[bool]
    """
    Select to prevent recently registered domains from triggering a Suspicious or
    Malicious disposition.
    """

    is_regex: Optional[bool]

    is_similarity: Optional[bool]
    """
    Select for partner or other approved domains that have similar spelling to your
    connected domains. Prevents listed domains from triggering a Spoof disposition.
    """

    pattern: Optional[str]
