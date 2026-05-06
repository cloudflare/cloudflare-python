# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["BillingInvoiceHistoryParams"]


class BillingInvoiceHistoryParams(TypedDict, total=False):
    account_id: Required[str]

    type: Literal["auto", "all", "manual"]
    """Filter invoice type: auto, manual, or all."""
