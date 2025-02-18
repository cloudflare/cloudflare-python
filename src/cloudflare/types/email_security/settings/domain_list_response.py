# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["DomainListResponse", "Authorization", "EmailsProcessed"]


class Authorization(BaseModel):
    authorized: bool

    timestamp: datetime

    status_message: Optional[str] = None


class EmailsProcessed(BaseModel):
    timestamp: datetime

    total_emails_processed: int

    total_emails_processed_previous: int


class DomainListResponse(BaseModel):
    id: int
    """The unique identifier for the domain."""

    allowed_delivery_modes: List[Literal["DIRECT", "BCC", "JOURNAL", "API", "RETRO_SCAN"]]

    created_at: datetime

    domain: str

    drop_dispositions: List[
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

    ip_restrictions: List[str]

    last_modified: datetime

    lookback_hops: int

    transport: str

    authorization: Optional[Authorization] = None

    emails_processed: Optional[EmailsProcessed] = None

    folder: Optional[Literal["AllItems", "Inbox"]] = None

    inbox_provider: Optional[Literal["Microsoft", "Google"]] = None

    integration_id: Optional[str] = None

    o365_tenant_id: Optional[str] = None

    require_tls_inbound: Optional[bool] = None

    require_tls_outbound: Optional[bool] = None
