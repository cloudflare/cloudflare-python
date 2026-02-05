# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["ApprovalGroup"]


class ApprovalGroup(BaseModel):
    """A group of email addresses that can approve a temporary authentication request."""

    approvals_needed: float
    """The number of approvals needed to obtain access."""

    email_addresses: Optional[List[str]] = None
    """A list of emails that can approve the access request."""

    email_list_uuid: Optional[str] = None
    """The UUID of an re-usable email list."""
