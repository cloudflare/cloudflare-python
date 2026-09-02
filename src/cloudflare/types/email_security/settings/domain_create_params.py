# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["DomainCreateParams"]


class DomainCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    allowed_delivery_modes: Required[List[Literal["DIRECT", "BCC", "JOURNAL", "API", "RETRO_SCAN"]]]

    domain: Required[str]

    drop_dispositions: Required[
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
    ]

    ip_restrictions: Required[SequenceNotStr[str]]

    regions: Required[List[Literal["GLOBAL", "AU", "DE", "IN", "US"]]]

    folder: Optional[Literal["AllItems", "Inbox"]]

    integration_id: Optional[str]

    lookback_hops: Optional[int]

    require_tls_inbound: Optional[bool]

    require_tls_outbound: Optional[bool]

    transport: Optional[str]
