# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ConfigCreateParams"]


class ConfigCreateParams(TypedDict, total=False):
    account_id: Required[str]

    amount: Required[int]
    """Auto top-up amount in cents (min 1000)."""

    threshold: Required[int]
    """Balance threshold in cents that triggers auto top-up (min 500)."""
