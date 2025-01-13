# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["AppUpdateParams"]


class AppUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    hostnames: List[str]
    """FQDNs to associate with traffic decisions."""

    ip_subnets: List[str]
    """CIDRs to associate with traffic decisions."""

    name: str
    """Display name for the app."""

    type: str
    """Category of the app."""
