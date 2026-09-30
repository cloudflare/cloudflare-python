# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["DomainEditParams"]


class DomainEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    allowed_delivery_modes: List[Literal["DIRECT", "BCC", "JOURNAL", "API", "RETRO_SCAN"]]
    """Delivery modes to onboard the domain through."""

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
    """Dispositions to drop instead of delivering, e.g. `["MALICIOUS", "SPAM"]`."""

    folder: Optional[Literal["AllItems", "Inbox"]]
    """The mailbox folder to scan, for API-scanning domains."""

    integration_id: Optional[str]
    """Identifier of the CASB integration that authorizes this domain.

    The integration also enables API scanning, post-delivery actions, and directory
    sync.
    """

    ip_restrictions: SequenceNotStr[str]
    """Source IP ranges mail is accepted from. Any other source is rejected."""

    lookback_hops: int
    """
    Number of hops to trace back through received headers when reconstructing the
    original message (1-20).
    """

    regions: List[Literal["GLOBAL", "AU", "DE", "IN", "US"]]
    """Regions that process messages for this domain, e.g. `["GLOBAL"]` or `["US"]`."""

    require_tls_inbound: bool
    """Require TLS on inbound connections."""

    require_tls_outbound: bool
    """Require TLS on outbound connections."""

    transport: str
    """
    The mail transport hostname for MX/Inline delivery — the MX record Cloudflare
    delivers email to (e.g. `mx.example.com`).
    """
