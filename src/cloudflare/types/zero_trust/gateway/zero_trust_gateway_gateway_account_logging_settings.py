# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...shared import UnnamedSchemaRef28
from ...._models import BaseModel

__all__ = ["ZeroTrustGatewayGatewayAccountLoggingSettings"]


class ZeroTrustGatewayGatewayAccountLoggingSettings(BaseModel):
    redact_pii: Optional[bool] = None
    """
    Redact personally identifiable information from activity logging (PII fields
    are: source IP, user email, user ID, device ID, URL, referrer, user agent).
    """

    settings_by_rule_type: Optional[UnnamedSchemaRef28] = None
    """Logging settings by rule type."""
