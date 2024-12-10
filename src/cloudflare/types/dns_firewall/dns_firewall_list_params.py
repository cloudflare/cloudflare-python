# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DNSFirewallListParams"]


class DNSFirewallListParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    page: float
    """Page number of paginated results"""

    per_page: float
    """Number of clusters per page"""
