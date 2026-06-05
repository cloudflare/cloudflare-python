# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["AccountGetResponse"]


class AccountGetResponse(BaseModel):
    record_quota: Optional[int] = None
    """Maximum number of DNS records allowed across all public zones in the account.

    Null if using zone-level quota.
    """

    record_usage: int
    """Current number of DNS records across all public zones in the account."""

    internal_record_quota: Optional[int] = None
    """Maximum number of DNS records allowed across all internal zones in the account.

    Only present if internal DNS is enabled.
    """

    internal_record_usage: Optional[int] = None
    """Current number of DNS records across all internal zones in the account.

    Only present if internal DNS is enabled.
    """
