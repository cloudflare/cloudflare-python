# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["CTAlertingSubscription"]


class CTAlertingSubscription(BaseModel):
    """Certificate Transparency alerting subscription settings for a zone."""

    enabled: bool
    """Whether CT alerting is enabled for the zone."""

    emails: Optional[List[str]] = None
    """Email addresses that receive CT alert notifications for the zone.

    A maximum of 100 addresses may be configured. Each address must be a valid RFC
    5322 email address and must not contain a comma.
    """
