# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TopupStatusParams"]


class TopupStatusParams(TypedDict, total=False):
    account_id: Required[str]

    payment_intent_id: Required[str]
    """Stripe invoice ID to check status for."""
