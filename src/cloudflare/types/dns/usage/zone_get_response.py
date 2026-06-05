# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["ZoneGetResponse"]


class ZoneGetResponse(BaseModel):
    record_quota: Optional[int] = None
    """Maximum number of DNS records allowed for the zone.

    Null if using account-level quota.
    """

    record_usage: int
    """Current number of DNS records in the zone."""
