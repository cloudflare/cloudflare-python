# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["AddressingIpamDelegations"]


class AddressingIpamDelegations(BaseModel):
    id: Optional[str] = None
    """Delegation identifier tag."""

    cidr: Optional[str] = None
    """IP Prefix in Classless Inter-Domain Routing format."""

    created_at: Optional[datetime] = None

    delegated_account_id: Optional[str] = None
    """Account identifier for the account to which prefix is being delegated."""

    modified_at: Optional[datetime] = None

    parent_prefix_id: Optional[str] = None
    """Identifier"""
