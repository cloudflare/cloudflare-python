# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["AppDeleteResponse"]


class AppDeleteResponse(BaseModel):
    account_app_id: str
    """Magic account app ID."""

    hostnames: Optional[List[str]] = None
    """FQDNs to associate with traffic decisions."""

    ip_subnets: Optional[List[str]] = None
    """CIDRs to associate with traffic decisions."""

    name: Optional[str] = None
    """Display name for the app."""

    type: Optional[str] = None
    """Category of the app."""
