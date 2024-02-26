# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["VerificationListParams"]


class VerificationListParams(TypedDict, total=False):
    retry: Literal[True]
    """Immediately retry SSL Verification."""
