# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["SendingDomainRestrictionCreateParams"]


class SendingDomainRestrictionCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    domain: Required[str]
    """Domain that requires TLS enforcement."""

    exclude: Required[SequenceNotStr[str]]
    """Excluded subdomains that are exempt from TLS requirements."""

    comments: Optional[str]
