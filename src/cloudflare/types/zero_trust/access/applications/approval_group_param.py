# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["ApprovalGroupParam"]


class ApprovalGroupParam(TypedDict, total=False):
    approvals_needed: Required[float]
    """The number of approvals needed to obtain access."""

    email_addresses: List[str]
    """A list of emails that can approve the access request."""

    email_list_uuid: str
    """The UUID of an re-usable email list."""
