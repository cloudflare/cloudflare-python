# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["DomainEditResponse", "Authorization", "EmailsProcessed"]


class Authorization(BaseModel):
    authorized: bool

    timestamp: datetime

    status_message: Optional[str] = None


class EmailsProcessed(BaseModel):
    timestamp: datetime

    total_emails_processed: int

    total_emails_processed_previous: int


class DomainEditResponse(BaseModel):
    id: Optional[str] = None
    """Domain identifier"""

    allowed_delivery_modes: Optional[List[Literal["DIRECT", "BCC", "JOURNAL", "API", "RETRO_SCAN"]]] = None

    authorization: Optional[Authorization] = None

    created_at: Optional[datetime] = None

    dmarc_status: Optional[Literal["none", "good", "invalid"]] = None

    domain: Optional[str] = None

    drop_dispositions: Optional[
        List[
            Literal[
                "MALICIOUS",
                "MALICIOUS-BEC",
                "SUSPICIOUS",
                "SPOOF",
                "SPAM",
                "BULK",
                "ENCRYPTED",
                "EXTERNAL",
                "UNKNOWN",
                "NONE",
            ]
        ]
    ] = None

    emails_processed: Optional[EmailsProcessed] = None

    folder: Optional[Literal["AllItems", "Inbox"]] = None

    inbox_provider: Optional[Literal["Microsoft", "Google"]] = None

    integration_id: Optional[str] = None

    ip_restrictions: Optional[List[str]] = None

    last_modified: Optional[datetime] = None
    """Deprecated, use `modified_at` instead. End of life: November 1, 2026."""

    lookback_hops: Optional[int] = None

    modified_at: Optional[datetime] = None

    o365_tenant_id: Optional[str] = None

    regions: Optional[List[Literal["GLOBAL", "AU", "DE", "IN", "US"]]] = None

    require_tls_inbound: Optional[bool] = None

    require_tls_outbound: Optional[bool] = None

    spf_status: Optional[Literal["none", "good", "neutral", "open", "invalid"]] = None

    status: Optional[Literal["pending", "active", "failed", "timeout"]] = None

    transport: Optional[str] = None
