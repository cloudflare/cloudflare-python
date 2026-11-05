# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["ConfigCreateParams", "Variant0", "Variant1"]


class Variant0(TypedDict, total=False):
    account_id: Required[str]

    amount: Required[int]
    """Auto top-up amount in cents (min 1000)."""

    threshold: Required[int]
    """Balance threshold in cents that triggers auto top-up (min 500)."""


class Variant1(TypedDict, total=False):
    account_id: Required[str]

    amount: Required[int]
    """Auto top-up amount in cents (min 1000)."""

    consent_version: Required[str]
    """Version of the off-session auto-top-up consent accepted by the user."""

    payment_method_id: Required[str]
    """Card to authenticate for future automatic top-ups."""

    setup_idempotency_key: Required[str]
    """Client-generated UUID that makes payment-method setup safe to retry."""

    threshold: Required[int]
    """Balance threshold in cents that triggers auto top-up (min 500)."""

    setup_intent_id: str
    """Successfully confirmed payment-method setup identifier."""


ConfigCreateParams: TypeAlias = Union[Variant0, Variant1]
