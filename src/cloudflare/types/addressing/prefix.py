# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["Prefix"]


class Prefix(BaseModel):
    id: Optional[str] = None
    """Identifier of an IP Prefix."""

    account_id: Optional[str] = None
    """Identifier of a Cloudflare account."""

    advertised: Optional[bool] = None
    """Prefix advertisement status to the Internet.

    This field is only not 'null' if on demand is enabled.
    """

    advertised_modified_at: Optional[datetime] = None
    """Last time the advertisement status was changed.

    This field is only not 'null' if on demand is enabled.
    """

    approved: Optional[str] = None
    """Approval state of the prefix (P = pending, V = active)."""

    asn: Optional[int] = None
    """Autonomous System Number (ASN) the prefix will be advertised under."""

    cidr: Optional[str] = None
    """IP Prefix in Classless Inter-Domain Routing format."""

    created_at: Optional[datetime] = None

    description: Optional[str] = None
    """Description of the prefix."""

    loa_document_id: Optional[str] = None
    """Identifier for the uploaded LOA document."""

    modified_at: Optional[datetime] = None

    on_demand_enabled: Optional[bool] = None
    """
    Whether advertisement of the prefix to the Internet may be dynamically enabled
    or disabled.
    """

    on_demand_locked: Optional[bool] = None
    """
    Whether advertisement status of the prefix is locked, meaning it cannot be
    changed.
    """
