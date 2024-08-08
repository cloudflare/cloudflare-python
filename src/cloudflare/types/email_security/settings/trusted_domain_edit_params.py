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

    is_regex: Optional[bool]

    is_similarity: Optional[bool]

    pattern: Optional[str]
