# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TopupCreateParams"]


class TopupCreateParams(TypedDict, total=False):
    account_id: Required[str]

    amount: Required[int]
    """Top-up amount in cents (min 1000)."""
