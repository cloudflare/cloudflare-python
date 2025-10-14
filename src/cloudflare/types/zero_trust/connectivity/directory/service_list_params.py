# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ServiceListParams"]


class ServiceListParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier"""

    page: int
    """Current page in the response"""

    per_page: int
    """Max amount of entries returned per page"""

    type: Optional[Literal["http"]]
