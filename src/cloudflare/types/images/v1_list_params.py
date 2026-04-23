# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["V1ListParams"]


class V1ListParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier tag."""

    creator: Optional[str]
    """Internal user ID set within the creator field.

    Setting to empty string "" will return images where creator field is not set
    """

    page: float
    """Page number of paginated results."""

    per_page: float
    """Number of items per page."""
