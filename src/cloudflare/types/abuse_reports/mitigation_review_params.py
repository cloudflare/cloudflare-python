# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["MitigationReviewParams", "Appeal"]


class MitigationReviewParams(TypedDict, total=False):
    account_id: Required[str]

    appeals: Required[Iterable[Appeal]]
    """List of mitigations to appeal."""


class Appeal(TypedDict, total=False):
    id: Required[str]
    """ID of the mitigation to appeal."""

    reason: Required[Literal["removed", "misclassified"]]
    """Reason why the customer is appealing."""
