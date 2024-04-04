# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel
from .unnamed_schema_ref_e86eeb84b7e922c35cfb0031a6309f7b import UnnamedSchemaRefE86eeb84b7e922c35cfb0031a6309f7b

__all__ = ["ZeroTrustGatewayGatewayAccountLoggingSettings"]


class ZeroTrustGatewayGatewayAccountLoggingSettings(BaseModel):
    redact_pii: Optional[bool] = None
    """
    Redact personally identifiable information from activity logging (PII fields
    are: source IP, user email, user ID, device ID, URL, referrer, user agent).
    """

    settings_by_rule_type: Optional[UnnamedSchemaRefE86eeb84b7e922c35cfb0031a6309f7b] = None
    """Logging settings by rule type."""
