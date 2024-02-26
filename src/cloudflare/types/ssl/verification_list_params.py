# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["VerificationListParams"]


class VerificationListParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    retry: Literal[True]
    """Immediately retry SSL Verification."""
