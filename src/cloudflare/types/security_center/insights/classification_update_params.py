# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["ClassificationUpdateParams"]


class ClassificationUpdateParams(TypedDict, total=False):
    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    classification: Optional[Literal["false_positive", "accept_risk", "other"]]
    """User-defined classification for the insight.

    Can be 'false_positive', 'accept_risk', 'other', or null.
    """

    rationale: str
    """Rationale for the classification change.

    Required when classification is 'accept_risk' or 'other'.
    """
