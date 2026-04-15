# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["MTLSCertificateListParams"]


class MTLSCertificateListParams(TypedDict, total=False):
    account_id: str
    """Identifier."""

    type: List[Literal["custom", "gateway_managed", "access_managed"]]
    """Filters results by certificate type. Multiple types can be comma-separated."""
