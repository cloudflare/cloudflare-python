# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["AlertingGetResponse"]


class AlertingGetResponse(BaseModel):
    """Certificate Transparency alerting subscription settings for a zone."""

    enabled: bool
    """Whether CT alerting is enabled for the zone."""

    emails: Optional[List[str]] = None
    """Email addresses that receive CT alert notifications.

    Only present and configurable for Business and Enterprise zones. Maximum of 10
    addresses. For Free and Pro zones, notifications are sent to all users with SSL
    permissions on the zone.
    """
